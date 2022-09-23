#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yelp
Version  : 42.2
Release  : 34
URL      : https://download.gnome.org/sources/yelp/42/yelp-42.2.tar.xz
Source0  : https://download.gnome.org/sources/yelp/42/yelp-42.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: yelp-bin = %{version}-%{release}
Requires: yelp-data = %{version}-%{release}
Requires: yelp-lib = %{version}-%{release}
Requires: yelp-license = %{version}-%{release}
Requires: yelp-locales = %{version}-%{release}
Requires: gnome-getting-started-docs
Requires: yelp-xsl
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gsettings-desktop-schemas
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-unix-print-3.0)
BuildRequires : pkgconfig(libexslt)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(yelp-xsl)
BuildRequires : webkitgtk-dev

%description
This is a copy of a subset of the files in the MathJax repository:
https://github.com/mathjax/mathjax/

%package bin
Summary: bin components for the yelp package.
Group: Binaries
Requires: yelp-data = %{version}-%{release}
Requires: yelp-license = %{version}-%{release}

%description bin
bin components for the yelp package.


%package data
Summary: data components for the yelp package.
Group: Data

%description data
data components for the yelp package.


%package dev
Summary: dev components for the yelp package.
Group: Development
Requires: yelp-lib = %{version}-%{release}
Requires: yelp-bin = %{version}-%{release}
Requires: yelp-data = %{version}-%{release}
Provides: yelp-devel = %{version}-%{release}
Requires: yelp = %{version}-%{release}

%description dev
dev components for the yelp package.


%package lib
Summary: lib components for the yelp package.
Group: Libraries
Requires: yelp-data = %{version}-%{release}
Requires: yelp-license = %{version}-%{release}

%description lib
lib components for the yelp package.


%package license
Summary: license components for the yelp package.
Group: Default

%description license
license components for the yelp package.


%package locales
Summary: locales components for the yelp package.
Group: Default

%description locales
locales components for the yelp package.


%prep
%setup -q -n yelp-42.2
cd %{_builddir}/yelp-42.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663605195
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1663605195
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yelp
cp %{_builddir}/yelp-%{version}/COPYING %{buildroot}/usr/share/package-licenses/yelp/ebc45949d86ed28d87b1dd4d9d866bd4667c87ff || :
cp %{_builddir}/yelp-%{version}/data/mathjax/LICENSE %{buildroot}/usr/share/package-licenses/yelp/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
%make_install
%find_lang yelp

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-help
/usr/bin/yelp

%files data
%defattr(-,root,root,-)
/usr/share/applications/yelp.desktop
/usr/share/glib-2.0/schemas/org.gnome.yelp.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Yelp.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Yelp-symbolic.svg
/usr/share/metainfo/yelp.appdata.xml
/usr/share/yelp-xsl/xslt/common/domains/yelp.xml
/usr/share/yelp/dtd/catalog
/usr/share/yelp/dtd/docbookx.dtd
/usr/share/yelp/dtd/isoamsa.ent
/usr/share/yelp/dtd/isoamsb.ent
/usr/share/yelp/dtd/isoamsc.ent
/usr/share/yelp/dtd/isoamsn.ent
/usr/share/yelp/dtd/isoamso.ent
/usr/share/yelp/dtd/isoamsr.ent
/usr/share/yelp/dtd/isobox.ent
/usr/share/yelp/dtd/isocyr1.ent
/usr/share/yelp/dtd/isocyr2.ent
/usr/share/yelp/dtd/isodia.ent
/usr/share/yelp/dtd/isogrk1.ent
/usr/share/yelp/dtd/isogrk2.ent
/usr/share/yelp/dtd/isogrk3.ent
/usr/share/yelp/dtd/isogrk4.ent
/usr/share/yelp/dtd/isolat1.ent
/usr/share/yelp/dtd/isolat2.ent
/usr/share/yelp/dtd/isonum.ent
/usr/share/yelp/dtd/isopub.ent
/usr/share/yelp/dtd/isotech.ent
/usr/share/yelp/icons/hicolor/16x16/status/bookmark.png
/usr/share/yelp/icons/hicolor/16x16/status/yelp-page-task.png
/usr/share/yelp/icons/hicolor/16x16/status/yelp-page-tip.png
/usr/share/yelp/icons/hicolor/16x16/status/yelp-page-ui.png
/usr/share/yelp/icons/hicolor/16x16/status/yelp-page-video.png
/usr/share/yelp/icons/hicolor/scalable/status/yelp-page-problem-symbolic.svg
/usr/share/yelp/icons/hicolor/scalable/status/yelp-page-search-symbolic.svg
/usr/share/yelp/icons/hicolor/scalable/status/yelp-page-symbolic.svg
/usr/share/yelp/icons/hicolor/scalable/status/yelp-page-task-symbolic.svg
/usr/share/yelp/icons/hicolor/scalable/status/yelp-page-tip-symbolic.svg
/usr/share/yelp/icons/hicolor/scalable/status/yelp-page-ui-symbolic.svg
/usr/share/yelp/icons/hicolor/scalable/status/yelp-page-video-symbolic.svg
/usr/share/yelp/mathjax/MathJax.js
/usr/share/yelp/mathjax/config/MMLorHTML.js
/usr/share/yelp/mathjax/config/yelp.js
/usr/share/yelp/mathjax/extensions/HTML-CSS/handle-floats.js
/usr/share/yelp/mathjax/extensions/MathEvents.js
/usr/share/yelp/mathjax/extensions/MathMenu.js
/usr/share/yelp/mathjax/extensions/MathZoom.js
/usr/share/yelp/mathjax/extensions/mml2jax.js
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_AMS-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Bold.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Fraktur-Bold.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Fraktur-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-BoldItalic.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_SansSerif-Bold.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_SansSerif-Italic.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_SansSerif-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Script-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff
/usr/share/yelp/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Typewriter-Regular.woff
/usr/share/yelp/mathjax/jax/element/mml/jax.js
/usr/share/yelp/mathjax/jax/element/mml/optable/Arrows.js
/usr/share/yelp/mathjax/jax/element/mml/optable/BasicLatin.js
/usr/share/yelp/mathjax/jax/element/mml/optable/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/element/mml/optable/CombDiactForSymbols.js
/usr/share/yelp/mathjax/jax/element/mml/optable/Dingbats.js
/usr/share/yelp/mathjax/jax/element/mml/optable/GeneralPunctuation.js
/usr/share/yelp/mathjax/jax/element/mml/optable/GeometricShapes.js
/usr/share/yelp/mathjax/jax/element/mml/optable/GreekAndCoptic.js
/usr/share/yelp/mathjax/jax/element/mml/optable/Latin1Supplement.js
/usr/share/yelp/mathjax/jax/element/mml/optable/LetterlikeSymbols.js
/usr/share/yelp/mathjax/jax/element/mml/optable/MathOperators.js
/usr/share/yelp/mathjax/jax/element/mml/optable/MiscMathSymbolsA.js
/usr/share/yelp/mathjax/jax/element/mml/optable/MiscMathSymbolsB.js
/usr/share/yelp/mathjax/jax/element/mml/optable/MiscSymbolsAndArrows.js
/usr/share/yelp/mathjax/jax/element/mml/optable/MiscTechnical.js
/usr/share/yelp/mathjax/jax/element/mml/optable/SpacingModLetters.js
/usr/share/yelp/mathjax/jax/element/mml/optable/SuppMathOperators.js
/usr/share/yelp/mathjax/jax/element/mml/optable/SupplementalArrowsA.js
/usr/share/yelp/mathjax/jax/element/mml/optable/SupplementalArrowsB.js
/usr/share/yelp/mathjax/jax/input/MathML/config.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/a.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/b.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/c.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/d.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/e.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/f.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/fr.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/g.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/h.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/i.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/j.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/k.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/l.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/m.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/n.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/o.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/opf.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/p.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/q.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/r.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/s.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/scr.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/t.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/u.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/v.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/w.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/x.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/y.js
/usr/share/yelp/mathjax/jax/input/MathML/entities/z.js
/usr/share/yelp/mathjax/jax/input/MathML/jax.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/annotation-xml.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/maction.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/menclose.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/mglyph.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/mmultiscripts.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/ms.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/mtable.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/autoload/multiline.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/config.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/Arrows.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/BBBold.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/BoxDrawing.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/Dingbats.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/EnclosedAlphanum.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/GeneralPunctuation.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/GeometricShapes.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/GreekAndCoptic.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/Latin1Supplement.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/LatinExtendedA.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/LetterlikeSymbols.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/MathOperators.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/MiscMathSymbolsB.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/MiscSymbols.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/MiscTechnical.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/PUA.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/SpacingModLetters.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/AMS/Regular/SuppMathOperators.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Caligraphic/Bold/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Caligraphic/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Bold/BasicLatin.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Bold/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Bold/Other.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Bold/PUA.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Regular/BasicLatin.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Regular/Other.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Fraktur/Regular/PUA.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Greek/Bold/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Greek/BoldItalic/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Greek/Italic/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Greek/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/Arrows.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/CombDiactForSymbols.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/GeneralPunctuation.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/GeometricShapes.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/Latin1Supplement.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/LatinExtendedA.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/LatinExtendedB.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/LetterlikeSymbols.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/MathOperators.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/MiscMathSymbolsA.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/MiscSymbols.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/MiscTechnical.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/SpacingModLetters.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/SuppMathOperators.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Bold/SupplementalArrowsA.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Italic/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Italic/GeneralPunctuation.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Italic/Latin1Supplement.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Italic/LetterlikeSymbols.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Italic/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Regular/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Regular/GeometricShapes.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Regular/MiscSymbols.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Main/Regular/SpacingModLetters.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Math/BoldItalic/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Math/Italic/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Bold/BasicLatin.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Bold/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Bold/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Bold/Other.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Italic/BasicLatin.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Italic/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Italic/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Italic/Other.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Regular/BasicLatin.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Regular/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/SansSerif/Regular/Other.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Script/Regular/BasicLatin.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Script/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Script/Regular/Other.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Size1/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Size2/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Size3/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Size4/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Typewriter/Regular/BasicLatin.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Typewriter/Regular/CombDiacritMarks.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Typewriter/Regular/Main.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/Typewriter/Regular/Other.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/fontdata-extra.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/fonts/TeX/fontdata.js
/usr/share/yelp/mathjax/jax/output/HTML-CSS/jax.js
/usr/share/yelp/mathjax/jax/output/NativeMML/config.js
/usr/share/yelp/mathjax/jax/output/NativeMML/jax.js
/usr/share/yelp/xslt/db2html.xsl
/usr/share/yelp/xslt/info2html.xsl
/usr/share/yelp/xslt/links2html.xsl
/usr/share/yelp/xslt/mal2html.xsl
/usr/share/yelp/xslt/man2html.xsl
/usr/share/yelp/xslt/yelp-common.xsl

%files dev
%defattr(-,root,root,-)
/usr/include/libyelp/yelp-bookmarks.h
/usr/include/libyelp/yelp-docbook-document.h
/usr/include/libyelp/yelp-document.h
/usr/include/libyelp/yelp-help-list.h
/usr/include/libyelp/yelp-info-document.h
/usr/include/libyelp/yelp-mallard-document.h
/usr/include/libyelp/yelp-man-document.h
/usr/include/libyelp/yelp-search-entry.h
/usr/include/libyelp/yelp-settings.h
/usr/include/libyelp/yelp-simple-document.h
/usr/include/libyelp/yelp-sqlite-storage.h
/usr/include/libyelp/yelp-storage.h
/usr/include/libyelp/yelp-transform.h
/usr/include/libyelp/yelp-types.h
/usr/include/libyelp/yelp-uri-builder.h
/usr/include/libyelp/yelp-uri.h
/usr/include/libyelp/yelp-view.h
/usr/lib64/libyelp.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libyelp.so.0
/usr/lib64/libyelp.so.0.0.0
/usr/lib64/yelp/web-extensions/libyelpwebextension.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yelp/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/yelp/ebc45949d86ed28d87b1dd4d9d866bd4667c87ff

%files locales -f yelp.lang
%defattr(-,root,root,-)

