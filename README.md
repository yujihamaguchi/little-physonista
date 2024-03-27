# memo (2024/3/27 時点の情報です。管理は任せますが、読んで理解したものは消す感じで見ていただければ)
- CI/CD パイプライン
  - リソースの場所
    - パイプラインを定義している yaml ファイルは[リポジトリ](https://dev.azure.com/Japan-Apps-and-Infra/_git/SOMPO-HD-DevOps) の pipeline ディレクトリ配下でバージョン管理しています
    - パラメータとその値は各パイプラインの定義の Variables に格納しています（例: [CI パイプラインの編集画面](https://dev.azure.com/Japan-Apps-and-Infra/SOMPO-HD-DevOps/_apps/hub/ms.vss-build-web.ci-designer-hub?pipelineId=10&branch=main)）
    - 環境は [Pipelines > Environments](https://dev.azure.com/Japan-Apps-and-Infra/SOMPO-HD-DevOps/_environments) で定義しています
    - シークレットは [Pipelines > Library](https://dev.azure.com/Japan-Apps-and-Infra/SOMPO-HD-DevOps/_library?itemType=VariableGroups) で定義しています
  - テスト
    - 以下のシナリオが実行可能な状態を保っています（これらをリグレッションテストと見做しています）
      - Sprint 3 Review( p12 ): https://sompo-dl.box.com/s/67ge9k67urju2z8xs8305sh5qwybm83d
      - Sprint 4 Review( p17 ): https://sompo-dl.box.com/s/s185crtspx9uz7kr44mjpfp7v35sqcal
      - Sprint 5 Review( p15 ): https://sompo-dl.box.com/s/hfzxf4r9ovwaq7li3yvt27hq3g43y8rw
  - その他
    - 既存バージョンのパッケージの publish は失敗する仕様です。CI パイプラインを実行する際は、./transforms_sample/setup.cfg の metadata セクションの version を更新してください
    - CI パイプラインの DockerBuildAndPush で "##[warning]No data was written into the file /home/vsts/work/_temp/task_outputs/build_1711502963952.txt" のような警告がでますが、[Azure Pipeline Task のバグ](https://github.com/microsoft/azure-pipelines-tasks/issues/17893)のようです
    - PR パイプラインのトリガーは pr.yaml では none となっており、[main ブランチのポリシーの Build Validation](https://dev.azure.com/Japan-Apps-and-Infra/SOMPO-HD-DevOps/_settings/repositories?_a=policiesMid&repo=88b5906d-723f-4860-8785-d7c145770d64&refs=refs/heads/main)で設定しています。そういう習わしのようです
    - 想定 Foundry の Code Repository であるの外部リポジトリは、私個人の Github のリポジトリを使っています、使い続けて頂いても構いませんが、今の PAT の有効期限は 2024/6/8 です