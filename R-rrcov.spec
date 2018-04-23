#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rrcov
Version  : 1.4.3
Release  : 3
URL      : https://cran.r-project.org/src/contrib/rrcov_1.4-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rrcov_1.4-3.tar.gz
Summary  : Scalable Robust Estimators with High Breakdown Point
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-rrcov-lib
Requires: R-mclust
Requires: R-mvtnorm
Requires: R-pcaPP
Requires: R-robustbase
BuildRequires : R-mclust
BuildRequires : R-mvtnorm
BuildRequires : R-pcaPP
BuildRequires : R-robustbase
BuildRequires : clr-R-helpers

%description
Multivariate Analysis with High Breakdown Point.

%package lib
Summary: lib components for the R-rrcov package.
Group: Libraries

%description lib
lib components for the R-rrcov package.


%prep
%setup -q -c -n rrcov

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521270101

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521270101
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rrcov
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rrcov
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rrcov
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rrcov|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rrcov/CITATION
/usr/lib64/R/library/rrcov/DESCRIPTION
/usr/lib64/R/library/rrcov/INDEX
/usr/lib64/R/library/rrcov/Meta/Rd.rds
/usr/lib64/R/library/rrcov/Meta/data.rds
/usr/lib64/R/library/rrcov/Meta/features.rds
/usr/lib64/R/library/rrcov/Meta/hsearch.rds
/usr/lib64/R/library/rrcov/Meta/links.rds
/usr/lib64/R/library/rrcov/Meta/nsInfo.rds
/usr/lib64/R/library/rrcov/Meta/package.rds
/usr/lib64/R/library/rrcov/Meta/vignette.rds
/usr/lib64/R/library/rrcov/NAMESPACE
/usr/lib64/R/library/rrcov/R/rrcov
/usr/lib64/R/library/rrcov/R/rrcov.rdb
/usr/lib64/R/library/rrcov/R/rrcov.rdx
/usr/lib64/R/library/rrcov/bm/bm_lts.m
/usr/lib64/R/library/rrcov/bm/bm_mcd.m
/usr/lib64/R/library/rrcov/bm/bmlts.S
/usr/lib64/R/library/rrcov/bm/bmmcd.S
/usr/lib64/R/library/rrcov/data/Appalachia.rda
/usr/lib64/R/library/rrcov/data/Cascades.rda
/usr/lib64/R/library/rrcov/data/OsloTransect.rda
/usr/lib64/R/library/rrcov/data/bus.rda
/usr/lib64/R/library/rrcov/data/bushmiss.rda
/usr/lib64/R/library/rrcov/data/fish.rda
/usr/lib64/R/library/rrcov/data/hemophilia.rda
/usr/lib64/R/library/rrcov/data/lmom32.rda
/usr/lib64/R/library/rrcov/data/lmom33.rda
/usr/lib64/R/library/rrcov/data/maryo.rda
/usr/lib64/R/library/rrcov/data/pottery.rda
/usr/lib64/R/library/rrcov/data/rice.rda
/usr/lib64/R/library/rrcov/data/salmon.rda
/usr/lib64/R/library/rrcov/data/un86.rda
/usr/lib64/R/library/rrcov/data/wages.rda
/usr/lib64/R/library/rrcov/doc/index.html
/usr/lib64/R/library/rrcov/doc/rrcov.R
/usr/lib64/R/library/rrcov/doc/rrcov.Rnw
/usr/lib64/R/library/rrcov/doc/rrcov.pdf
/usr/lib64/R/library/rrcov/help/AnIndex
/usr/lib64/R/library/rrcov/help/aliases.rds
/usr/lib64/R/library/rrcov/help/paths.rds
/usr/lib64/R/library/rrcov/help/rrcov.rdb
/usr/lib64/R/library/rrcov/help/rrcov.rdx
/usr/lib64/R/library/rrcov/html/00Index.html
/usr/lib64/R/library/rrcov/html/R.css
/usr/lib64/R/library/rrcov/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rrcov/libs/rrcov.so
/usr/lib64/R/library/rrcov/libs/rrcov.so.avx2
/usr/lib64/R/library/rrcov/libs/rrcov.so.avx512
