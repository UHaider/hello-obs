all: hobs
hobs: helloobs.c
	gcc -o helloobs helloobs.c
install: hobs
	mkdir -p ${RPM_BUILD_ROOT}/usr/bin
	cp helloobs ${RPM_BUILD_ROOT}/usr/bin
