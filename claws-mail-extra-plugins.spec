
#TODO		-split plugins in to packages
#		-remove *others package

Summary:	Plugins for sylpheed-claws (Metapackage)
Summary(pl):	Wtyczki dla sylpheed-claws (metapakiet)
Name:		sylpheed-claws-extra-plugins
Version:	2.3.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	06b53d69913ea1c96fb154fa2686606a
URL:		http://claws.sylpheed.org/plugins.php
BuildRequires:	curl-devel
BuildRequires:	libgtkhtml-devel
BuildRequires:	perl-devel
BuildRequires:	sylpheed-claws-devel >= 2.1.0
BuildRequires:	synce-librapi2-devel
BuildRequires:	synce-libsynce-devel
Requires:	sylpheed-claws >= 2.1.0
Requires:	sylpheed-claws-plugin-gtkhtml2_viewer = %{version}-%{release}
Requires:	sylpheed-claws-plugin-maildir = %{version}-%{release}
Requires:	sylpheed-claws-plugin-smime = %{version}-%{release}
Requires:	sylpheed-claws-plugin-others = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugins_dir	%{_libdir}/sylpheed-claws/plugins

%description
Plugins for sylpheed-claws (metapackage).

%description -l pl
Wtyczki dla sylpheed-claws (metapakiet).

%package -n sylpheed-claws-plugin-gtkhtml2_viewer
Summary:	gtkhtml2_viewer plugin for sylpheed-claws
Summary(pl):	Wtyczka gtkhtml2_viewer dla sylpheed-claws
Group:		X11/Applications/Networking

%description -n sylpheed-claws-plugin-gtkhtml2_viewer
Renders HTML mail using the gtkhtml2 rendering widget.

%description -n sylpheed-claws-plugin-gtkhtml2_viewer -l pl
Wy¶wietla maile HTML u¿ywaj±c widgeta gtkhtml2.

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
Pozwala rozszyfrowywaæ, weryfikowaæ lub podpisywaæ i szyfrowaæ w³asn±
pocztê.

%package -n sylpheed-claws-plugin-others
Summary:	Few plugins for sylpheed-claws
Summary(pl):	Kilka dodatkowych wtyczek dla sylpheed-claws
Group:		X11/Applications/Networking

%description -n sylpheed-claws-plugin-others
Few plugins for sylpheed-claws.

%description -n sylpheed-claws-plugin-others -l pl
Kilka dodatkowych wtyczek dla sylpheed-claws.

%prep
%setup -q

%build
for i in `find * -maxdepth 0 -type d -print`; do
	cd "$i"
	%configure
	%{__make}
	cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

for i in `find * -maxdepth 0 -type d -print`; do
	%{__make} -C "$i" install \
		DESTDIR=$RPM_BUILD_ROOT
done

%find_lang gtkhtml2_viewer

%find_lang acpi_notifier
%find_lang rssyl
%find_lang vcalendar
cat acpi_notifier.lang rssyl.lang vcalendar.lang > others.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n sylpheed-claws-plugin-gtkhtml2_viewer -f gtkhtml2_viewer.lang
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

%files -n sylpheed-claws-plugin-others -f others.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugins_dir}/acpi_notifier.so
%attr(755,root,root) %{_plugins_dir}/att_remover.so
%attr(755,root,root) %{_plugins_dir}/cachesaver.so
%attr(755,root,root) %{_plugins_dir}/etpan-privacy.so
%attr(755,root,root) %{_plugins_dir}/fetchinfo_plugin.so
%attr(755,root,root) %{_plugins_dir}/fetchinfo_plugin_gtk.so
%attr(755,root,root) %{_plugins_dir}/mailmbox.so
%attr(755,root,root) %{_plugins_dir}/newmail.so
%attr(755,root,root) %{_plugins_dir}/notification_plugin.so
%attr(755,root,root) %{_plugins_dir}/perl_plugin.so
%attr(755,root,root) %{_plugins_dir}/rssyl.so
%attr(755,root,root) %{_plugins_dir}/synce_plugin.so
%attr(755,root,root) %{_plugins_dir}/vcalendar.so
