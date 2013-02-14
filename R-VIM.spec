%global packname  VIM
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.0.3
Release:          1
Summary:          Visualization and Imputation of Missing Values
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/VIM_3.0.3.tar.gz
Requires:         R-e1071 R-car R-colorspace R-nnet R-robustbase R-tcltk
Requires:         R-tkrplot R-sp R-vcd R-Rcpp R-car R-colorspace R-grDevices
Requires:         R-robustbase R-stats R-tcltk R-sp R-utils R-vcd
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-e1071 R-car R-colorspace R-nnet R-robustbase R-tcltk
BuildRequires:    R-tkrplot R-sp R-vcd R-Rcpp R-car R-colorspace R-grDevices
BuildRequires:    R-robustbase R-stats R-tcltk R-sp R-utils R-vcd

%description
This package introduces new tools for the visualization of missing and/or
imputed values, which can be used for exploring the data and the structure
of the missing and/or imputed values. Depending on this structure of the
missing values, the corresponding methods may help to identify the
mechanism generating the missings and allows to explore the data including
missing values.  In addition, the quality of imputation can be visually
explored using various univariate, bivariate, multiple and multivariate
plot methods.  A graphical user interface allows an easy handling of the
implemented plot methods.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#  When sourcing 'VIM-EU-SILC.R':
# Error: [tcl] invalid command name "toplevel".
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/tklibs
