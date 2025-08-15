# CHANGELOG


## v0.1.0 (2025-08-15)

### Chores

* chore: Add github workflow for publishing to pypi ([`ca7642d`](https://github.com/shirte/impynb/commit/ca7642df64ba005bd9009fe6a50c192f08caad3b))

* chore: Add github action for semantic release ([`cee86d9`](https://github.com/shirte/impynb/commit/cee86d9bf80aff4d4eee331d60a002bba8ccb035))

* chore: Add semantic release ([`a573117`](https://github.com/shirte/impynb/commit/a5731177cf72bcb0f567c815014e23efaa61df86))

* chore: Add missing type in conftest ([`9dfc91f`](https://github.com/shirte/impynb/commit/9dfc91f6d7d0b3649f0226900aed181a49c892e6))

* chore: Add gitignore file ([`7dadb66`](https://github.com/shirte/impynb/commit/7dadb66b97b4745a8b44c3eb5b694c58680579b7))

### Documentation

* docs: Add a license file ([`7300390`](https://github.com/shirte/impynb/commit/730039063fe86cbb64c0586a838f2e3dbe754791))

### Features

* feat: Add context manager for NotebookFinder ([`98e1b91`](https://github.com/shirte/impynb/commit/98e1b91c71b654d54d85f2676047a9ac00a216f1))

* feat: Introduce parameter 'skin_cell_tags' indicating skippable cells ([`2bb81a8`](https://github.com/shirte/impynb/commit/2bb81a8a4403b9db79523ad1965089cba8131031))

* feat: Populate repository ([`afd09ee`](https://github.com/shirte/impynb/commit/afd09ee9d12b9eb171aa750066a4c71c7817856b))

### Fixes

* fix: Simplify context parameters ([`8d93b27`](https://github.com/shirte/impynb/commit/8d93b278771733c998e9ff3a3c79fbec0e4971ab))

* fix: Enable using a custom event loop ([`b056076`](https://github.com/shirte/impynb/commit/b056076ca45f7a45387816a7ff271d22ee1d8b64))

* fix: Enable running async cells ([`84450ad`](https://github.com/shirte/impynb/commit/84450ad7c4e5583354831fe6fd9904acdbfb35d8))

### Refactoring

* refactor: Use config object to store settings ([`a5f9977`](https://github.com/shirte/impynb/commit/a5f997714ab2110868371b34d44d072c788987be))

* refactor: Adapt tests to context manager ([`9019bcb`](https://github.com/shirte/impynb/commit/9019bcbb2f798b861597b082dd961bb23ea06e4c))

* refactor: Make NotebookFinder a singleton ([`f72db88`](https://github.com/shirte/impynb/commit/f72db88e6d777825093d67fdc86d103826194a84))

* refactor: Extract function checking if a notebook cell should be executed ([`02a9864`](https://github.com/shirte/impynb/commit/02a986491276467ac116143008f3f8c19076e208))

### Testing

* test: Add test for custom event loops ([`5cbe6ac`](https://github.com/shirte/impynb/commit/5cbe6ac484dbd3b5e21b6b203efc7ec54d193a4a))

* test: Add tests for async cells ([`91a9334`](https://github.com/shirte/impynb/commit/91a9334ae5317c73e986f6da9fde842ff2a5c6df))

* test: Add tests for context manager ([`87b3052`](https://github.com/shirte/impynb/commit/87b30526a8e42294279ef8685d5c7016e335bb96))

* test: Check if skip_cell_tags are working ([`67972bb`](https://github.com/shirte/impynb/commit/67972bb80dd16ad489030bb1ae76c454fa90d326))

* test: Add fixture to clean imports ([`0817927`](https://github.com/shirte/impynb/commit/08179276fcf24ea749bb8d06b2e107a3bfc0e893))

* test: Test importing namespaced modules ([`f8907e5`](https://github.com/shirte/impynb/commit/f8907e530791fa9ddd8461542e43a929d6fc12b2))

* test: Check that module initializer __init__.ipynb is recognized ([`1957373`](https://github.com/shirte/impynb/commit/19573733b88aa69eb2dff2391e1beac3d9cd2ab7))

* test: Check that exceptions in notebooks are displayed correctly ([`efb98a1`](https://github.com/shirte/impynb/commit/efb98a1628d9383af72b9b0b73587618a40cdbe6))

* test: Test importing notebooks from submodules ([`c16611c`](https://github.com/shirte/impynb/commit/c16611cc5f72babc3948f8dde0abe2a66c2276ad))

* test: Test excluding cells from execution ([`6a93225`](https://github.com/shirte/impynb/commit/6a93225976a8c038ec69d5d35e76949cfe81a673))

* test: Test importing local modules from notebook ([`614224d`](https://github.com/shirte/impynb/commit/614224d4aac357f69cc6ac11a555487f87cf572d))

* test: Add basic test ([`f10d419`](https://github.com/shirte/impynb/commit/f10d419732c3a2ec85b0ae2970e8e93bfb85e9de))

* test: Create a test package ([`c59d938`](https://github.com/shirte/impynb/commit/c59d938b3aa29067cc6e9e2c2aaf5bf2193b979e))
