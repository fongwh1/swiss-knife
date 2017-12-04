Inject symbols via LD_PRELOAD
===
## Annotation

* LD_PRELOAD
    * "forces some libraries to be loaded for a program."
* ldd
    * check dynamic library path
* nm -D libXXX.so
    * check dynamic symbols of libXXX.so (or other binary)
* _GNU_SOURCE in transparent_injection.c
    * enable non-standard define "RTLD_NEXT" in dlfcn.h
* -ldl
    * link libdl for dlsym
    * (and other dynamic linking related function)

* Possible uses refered in [1]

1. [Dynamic linker tricks: Using LD_PRELOAD to cheat, inject features and investigate programs](https://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/)