Summary:	Plugins for sylpheed-claws
Summary(pl):	Wtyczki dla sylpheed-claws
Name:		sylpheed-claws-extra-plugins
Version:	2.2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.gz
# Source0-md5:	0e305f70bdfcb7968846d20f42da561f
URL:		http://claws.sylpheed.org/plugins.php
BuildRequires:	sylpheed-claws-devel >= 2.1.0
Requires:	sylpheed-claws >= 2.1.0
Requires:	sylpheed-claws-plugin-maildir >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for sylpheed-claws

%description -l pl
Wtyczki dla sylpheed-claws

%package -n sylpheed-claws-plugin-maildir
Summary:	Maildir++ Plugin for Sylpheed-Claws
Summary(pl):	Wtyczka Maildir++ dla Sylpheed-Claws
Group:		X11/Applications/Networking

%description -n sylpheed-claws-plugin-maildir
The Maildir++ plugin for Sylpheed-Claws provides direct access to
Maildir++ Mailboxes used by IMAP-Servers like Courier-IMAP, BincIMAP
or Dovecot without having all the IMAP overhead of a connection to
'localhost'.

%description -n sylpheed-claws-plugin-maildir -l pl
Wtyczka obs³ugi Maildir++ dla Sylpheed-Claws umo¿liwia bezpo¶redni
dostêp do skrzynek formatu Maildir++ u¿ywanych przez serwery IMAP, jak
np. Courier-IMAP, BincIMAP czy Dovecot bez narzutu zwi±zanego z
obs³ug± protoko³u IMAP przy po³±czeniu z "localhostem".

%package -n sylpheed-claws-plugin-smime
Summary:	S/MIME plugin for sylpheed-claws
Summary(pl):	Wtyczka S/MIME dla sylpheed-claws
Group:		X11/Applications/Networking

%description -n sylpheed-claws-plugin-smime
This plugin handles S/MIME signed and/or encrypted mails. You can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description -n sylpheed-claws-plugin-smime -l pl
Ta wtyczka obs³uguje podpisan± i/lub zaszyfrowan± pocztê S/MIME.
Mo¿esz rozszyfrowywaæ, weryfikowaæ lub podpisywaæ i szyfrowaæ w³asn±
pocztê.

%package -n sylpheed-claws-plugin-gtkhtml2_viewer
Summary:	gtkhtml2_viewer plugin for sylpheed-claws
Summary(pl):	Wtyczka gtkhtml2_viewer dla sylpheed-claws
Group:		X11/Applications/Networking

%description -n sylpheed-claws-plugin-gtkhtml2_viewer
Renders HTML mail using the gtkhtml2 rendering widget.

%description -n sylpheed-claws-plugin-gtkhtml2_viewer -l pl
Wy¶wietla maile HTML u¿ywaj±c widgetia gtkhtml2.

%define	_plugins_dir	%{_libdir}/sylpheed-claws/plugins

%prep
%setup -q

%build
cd maildir-*
%configure
%{__make}
cd ../

cd smime-*
%configure
%{__make}
cd ../

cd gtkhtml2_viewer-*
%configure
%{__make}
cd ../

%install
rm -rf $RPM_BUILD_ROOT

cd maildir-*
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../

cd smime-*
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../

cd gtkhtml2_viewer*
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n sylpheed-claws-plugin-gtkhtml2_viewer
%defattr(644,root,root,755)
%doc maildir-*/ChangeLog maildir-*/README
%attr(755,root,root) %{_plugins_dir}/gtkhtml2_viewer.so

%files -n sylpheed-claws-plugin-maildir
%defattr(644,root,root,755)
%doc maildir-*/ChangeLog maildir-*/README
%attr(755,root,root) %{_plugins_dir}/maildir.so

%files -n sylpheed-claws-plugin-smime
%defattr(644,root,root,755)
%doc smime-*/ChangeLog smime-*/README
%attr(755,root,root) %{_plugins_dir}/smime.so
