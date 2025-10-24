//go:build proto_operator_values
// +build proto_operator_values

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

// Configuration affecting Istio control plane installation version and shape.

package apis

import (
	"bytes"

	github_com_golang_protobuf_jsonpb "github.com/golang/protobuf/jsonpb" // nolint: depguard
	"istio.io/istio/pkg/util/protomarshal"
)

// nolint
var _ github_com_golang_protobuf_jsonpb.JSONPBUnmarshaler = &IntOrString{}

func (i *IntOrString) MarshalJSONPB(_ *github_com_golang_protobuf_jsonpb.Marshaler) ([]byte, error) {
	return i.MarshalJSON()
}

func (i *IntOrString) UnmarshalJSONPB(_ *github_com_golang_protobuf_jsonpb.Unmarshaler, value []byte) error {
	return i.UnmarshalJSON(value)
}

// MarshalJSON is a custom marshaler for Values
func (in *Values) MarshalJSON() ([]byte, error) {
	str, err := OperatorMarshaler.MarshalToString(in)
	return []byte(str), err
}

// UnmarshalJSON is a custom unmarshaler for Values
func (in *Values) UnmarshalJSON(b []byte) error {
	return OperatorUnmarshaler.Unmarshal(bytes.NewReader(b), in)
}

func (v *Values) UnmarshalYAML(yaml string) error {
	return protomarshal.ApplyYAML(yaml, v)
}

var (
	OperatorMarshaler   = &github_com_golang_protobuf_jsonpb.Marshaler{}
	OperatorUnmarshaler = &github_com_golang_protobuf_jsonpb.Unmarshaler{}
)
