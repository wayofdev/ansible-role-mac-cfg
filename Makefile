###
### Variables
###

### Playbook name
playbook ?= main.yml
inventory ?= inventory.yml
reqs ?= requirements.yml

### Lint yaml files
lint:
	ansible-lint
	yamllint .
.PHONY: lint

### List all hostnames
ls-host:
	ansible all -i $(inventory) -m shell -a "hostname;"
.PHONY: ls-host

### Check playbook syntax
check-syntax:
	ansible-playbook $(playbook) -i $(inventory) --syntax-check
.PHONY: check-syntax

### Install ansible dependencies
install-deps:
	ansible-galaxy install -r $(reqs)
.PHONY: install-deps
