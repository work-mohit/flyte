package main

import (
	"fmt"
	"os"

	"github.com/flyteorg/flyte/flytepropeller/cmd/kubectl-flyte/cmd"
	"github.com/flyteorg/flyte/flytestdlib/contextutils"
	"github.com/flyteorg/flyte/flytestdlib/promutils/labeled"
	_ "k8s.io/client-go/plugin/pkg/client/auth/gcp"
)

func init() {
	labeled.SetMetricKeys(contextutils.ProjectKey, contextutils.DomainKey, contextutils.WorkflowIDKey,
		contextutils.TaskIDKey)
}

func main() {

	rootCmd := cmd.NewFlyteCommand()
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
