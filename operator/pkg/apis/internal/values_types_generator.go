// Copyright Istio Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"bytes"
	"fmt"
	"go/ast"
	"go/format"
	"go/parser"
	"go/token"
	"log"
	"os"
	"strings"
)

func main() {
	src, err := os.ReadFile("values_types.pb.go")
	if err != nil {
		log.Fatal(err)
	}

	protoOperatorValuesBuildTagLines := []byte("//go:build proto_operator_values\n// +build proto_operator_values\n\n")
	nonprotoOperatorValuesBuildTagLines := []byte("//go:build !proto_operator_values\n// +build !proto_operator_values\n\n")

	if bytes.HasPrefix(src, []byte(protoOperatorValuesBuildTagLines)) {
		src = bytes.TrimPrefix(src, protoOperatorValuesBuildTagLines)
	} else {
		protoSrc := bytes.NewBuffer(nil)
		protoSrc.Write(protoOperatorValuesBuildTagLines)
		protoSrc.Write(src)
		os.WriteFile("values_types.pb.go", protoSrc.Bytes(), os.FileMode(0644))
	}

	nonprotoSrc := bytes.NewBuffer(nil)
	nonprotoSrc.Write(nonprotoOperatorValuesBuildTagLines)
	nonprotoSrc.Write(src)

	fset := token.NewFileSet()
	file, err := parser.ParseFile(fset, "values_types.pb.go", nonprotoSrc, parser.ParseComments)
	if err != nil {
		log.Fatal(err)
	}

	cmap := ast.NewCommentMap(fset, file, file.Comments)

	var decls []ast.Decl
	for _, d := range file.Decls {
		if visitRootDecl(d) {
			decls = append(decls, d)
		}
	}
	file.Decls = decls

	// remove unmapped comments
	file.Comments = cmap.Filter(file).Comments()

	var buf bytes.Buffer
	err = format.Node(&buf, fset, file)
	if err != nil {
		log.Fatal(err)
	}
	if err := os.WriteFile("values_types.go", buf.Bytes(), os.FileMode(0644)); err != nil {
		log.Fatal(err)
	}
}

var dropImports = map[string]bool{
	`"reflect"`: true,
	`"sync"`:    true,
	`"unsafe"`:  true,
}

func visitRootDecl(node ast.Node) (keep bool) {
	switch node := node.(type) {
	case *ast.Ident:
		fmt.Println("ident", node.Name)
		return true
	case *ast.FuncDecl:
		if strings.HasPrefix(node.Name.Name, "Get") {
			return true
		}
		return false
	case *ast.GenDecl:
		switch node.Tok {
		case token.IMPORT:
			var specs []ast.Spec
			for _, s := range node.Specs {
				spec := s.(*ast.ImportSpec)
				if !dropImports[spec.Path.Value] {
					specs = append(specs, s)
				}
			}
			node.Specs = specs
			return len(node.Specs) > 0
		case token.VAR, token.CONST:
			var specs []ast.Spec
			for _, s := range node.Specs {
				spec := s.(*ast.ValueSpec)
				if len(spec.Names) != 1 {
					panic("unexpected value specs length")
				}
				if isExported(spec.Names[0].Name) {
					specs = append(specs, s)
				}
			}
			node.Specs = specs
			return len(node.Specs) > 0
		case token.TYPE:
			if len(node.Specs) != 1 {
				panic("unexpected type specs length")
			}
			typeSpec := node.Specs[0].(*ast.TypeSpec)
			if isExported(typeSpec.Name.Name) {
				// TODO: drop unexported fields
				return true
			} else {
				return false
			}
		default:
			fmt.Println("unexpected decl", node.Tok)
		}
		return true
	default:
		fmt.Printf("%T\n", node)
		return true
	}
}

func isExported(name string) bool {
	c := name[:1]
	return c != "_" && c == strings.ToUpper(c)
}
