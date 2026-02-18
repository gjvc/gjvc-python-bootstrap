# Makefile

# ---------------------------------------------------------------------------------------------------

THIS := $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT := $(dir $(THIS))


# ---------------------------------------------------------------------------------------------------

DISTRO_ID := $(shell . /etc/os-release && echo $$ID)
DISTRO_VERSION := $(shell . /etc/os-release && echo $$VERSION_ID)
DISTRO_LIKE := $(shell . /etc/os-release && echo $$ID_LIKE)

ifeq ($(DISTRO_ID),debian)
ctags := ctags-exuberant
endif
ifeq ($(DISTRO_ID),redhat)
ctags := ctags
endif


# ---------------------------------------------------------------------------------------------------

tags ::
	@$(ctags) --recurse=yes src/python/main

dev-init ::
	@$(ROOT)/bin/dev-init

venv-freeze ::
	@$(ROOT)/bin/venv-freeze

venv-install ::
	@$(ROOT)/bin/venv-install



info ::
	@echo DISTRO_ID=\"$(DISTRO_ID)\"
	@echo DISTRO_VERSION=\"$(DISTRO_VERSION)\"
	@echo DISTRO_LIKE=\"$(DISTRO_LIKE)\"

