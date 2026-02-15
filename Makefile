
DISTRO_ID := $(shell . /etc/os-release && echo $$ID)
DISTRO_VERSION := $(shell . /etc/os-release && echo $$VERSION_ID)
DISTRO_LIKE := $(shell . /etc/os-release && echo $$ID_LIKE)

info ::
	@echo DISTRO_ID=\"$(DISTRO_ID)\"
	@echo DISTRO_VERSION=\"$(DISTRO_VERSION)\"
	@echo DISTRO_LIKE=\"$(DISTRO_LIKE)\"

tags ::
	@ctags-exuberant --recurse=yes src/python/main


