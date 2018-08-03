#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yelp
Version  : 3.28.1
Release  : 7
URL      : https://download.gnome.org/sources/yelp/3.28/yelp-3.28.1.tar.xz
Source0  : https://download.gnome.org/sources/yelp/3.28/yelp-3.28.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: yelp-bin
Requires: yelp-lib
Requires: yelp-data
Requires: yelp-license
Requires: yelp-locales
Requires: yelp-xsl
BuildRequires : appstream-glib
BuildRequires : bzip2-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-unix-print-3.0)
BuildRequires : pkgconfig(libexslt)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(webkit2gtk-4.0)
BuildRequires : pkgconfig(webkit2gtk-web-extension-4.0)
BuildRequires : pkgconfig(yelp-xsl)

%description
Yelp is the default help viewer for the GNOME desktop.  Yelp provides
a simple graphical interface for viewing Mallard, DocBook, HTML, man,
and info formatted documentation.  The name Yelp was suggested by Daniel
Lundin. Yelp is pronounced the same as the swedish word for 'help'.

%package bin
Summary: bin components for the yelp package.
Group: Binaries
Requires: yelp-data
Requires: yelp-license

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
Requires: yelp-lib
Requires: yelp-bin
Requires: yelp-data
Provides: yelp-devel

%description dev
dev components for the yelp package.


%package doc
Summary: doc components for the yelp package.
Group: Documentation

%description doc
doc components for the yelp package.


%package lib
Summary: lib components for the yelp package.
Group: Libraries
Requires: yelp-data
Requires: yelp-license

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
%setup -q -n yelp-3.28.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533313078
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1533313078
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/yelp
cp COPYING %{buildroot}/usr/share/doc/yelp/COPYING
cp data/mathjax/LICENSE %{buildroot}/usr/share/doc/yelp/data_mathjax_LICENSE
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

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libyelp/YelpDocument.html
/usr/share/gtk-doc/html/libyelp/YelpSettings.html
/usr/share/gtk-doc/html/libyelp/YelpSimpleDocument.html
/usr/share/gtk-doc/html/libyelp/YelpUri.html
/usr/share/gtk-doc/html/libyelp/YelpView.html
/usr/share/gtk-doc/html/libyelp/api-index-full.html
/usr/share/gtk-doc/html/libyelp/ch01.html
/usr/share/gtk-doc/html/libyelp/ch01s02.html
/usr/share/gtk-doc/html/libyelp/home.png
/usr/share/gtk-doc/html/libyelp/index.html
/usr/share/gtk-doc/html/libyelp/left-insensitive.png
/usr/share/gtk-doc/html/libyelp/left.png
/usr/share/gtk-doc/html/libyelp/libyelp-yelp-error.html
/usr/share/gtk-doc/html/libyelp/libyelp.devhelp2
/usr/share/gtk-doc/html/libyelp/object-tree.html
/usr/share/gtk-doc/html/libyelp/right-insensitive.png
/usr/share/gtk-doc/html/libyelp/right.png
/usr/share/gtk-doc/html/libyelp/style.css
/usr/share/gtk-doc/html/libyelp/up-insensitive.png
/usr/share/gtk-doc/html/libyelp/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libyelp.so.0
/usr/lib64/libyelp.so.0.0.0
/usr/lib64/yelp/web-extensions/libyelpwebextension.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/yelp/COPYING
/usr/share/doc/yelp/data_mathjax_LICENSE

%files locales -f yelp.lang
%defattr(-,root,root,-)

