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
	"encoding/json"

	"google.golang.org/protobuf/types/known/wrapperspb"

	"k8s.io/apimachinery/pkg/util/intstr"
)

// UnmarshalJSON implements the json.Unmarshaller interface.
func (i *IntOrString) UnmarshalJSON(value []byte) error {
	if value[0] == '"' {
		i.Type = int64(intstr.String)
		var s string
		err := json.Unmarshal(value, &s)
		if err != nil {
			return err
		}
		i.StrVal = &wrapperspb.StringValue{Value: s}
		return nil
	}
	i.Type = int64(intstr.Int)
	var s int32
	err := json.Unmarshal(value, &s)
	if err != nil {
		return err
	}
	i.IntVal = &wrapperspb.Int32Value{Value: s}
	return nil
}

func (i *IntOrString) MarshalJSON() ([]byte, error) {
	if i.IntVal != nil {
		return json.Marshal(i.IntVal.GetValue())
	}
	return json.Marshal(i.StrVal.GetValue())
}

func (i *IntOrString) ToKubernetes() intstr.IntOrString {
	if i.IntVal != nil {
		return intstr.FromInt32(i.GetIntVal().GetValue())
	}
	return intstr.FromString(i.GetStrVal().GetValue())
}
