
#TODO		-split plugins in to packages
#		-remove *others package

Summary:	Plugins for sylpheed-claws (Metapackage)
Summary(pl):	Wtyczki dla sylpheed-claws (Metapaczka)
Name:		sylpheed-claws-extra-plugins
Version:	2.2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.gz
# Source0-md5:	0e305f70bdfcb7968846d20f42da561f
URL:		http://claws.sylpheed.org/plugins.php
BuildRequires:	sylpheed-claws-devel >= 2.1.0
BuildRequires:	libgtkhtml-devel
BuildRequires:	synce-libsynce-devel
BuildRequires:	synce-librapi2-devel
Requires:	sylpheed-claws >= 2.1.0
Requires:	sylpheed-claws-plugin-maildir >= %{version}
Requires:	sylpheed-claws-plugin-gtkhtml2_viewer >= %{version}
Requires:	sylpheed-claws-plugin-smime >= %{version}
Requires:	sylpheed-claws-plugin-others >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for sylpheed-claws

%description -l pl
Wtyczki dla sylpheed-claws

%package -n sylpheed-claws-plugin-gtkhtml2_viewer
Summary:	gtkhtml2_viewer plugin for sylpheed-claws
Summary(pl):	Wtyczka gtkhtml2_viewer dla sylpheed-claws
Group:		X11/Applications/Networking

%description -n sylpheed-claws-plugin-gtkhtml2_viewer
Renders HTML mail using the gtkhtml2 rendering widget.

%description -n sylpheed-claws-plugin-gtkhtml2_viewer -l pl
Wy¶wietla maile HTML u¿ywaj±c widgetia gtkhtml2.

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

%package -n sylpheed-claws-plugin-others
Summary:	Few plugins for sylpheed-claws
Summary(pl):	Kilka dodatkowych wtyczek dla sylpheed-claws
Group:		X11/Applications/Networking

%description -n sylpheed-claws-plugin-others
Few plugins for sylpheed-claws.

%define	_plugins_dir	%{_libdir}/sylpheed-claws/plugins

%prep
%setup -q

%build
for i in `find * -maxdepth 0 -type d -print`; do
	cd "$i"
	%configure
	%{__make}
	cd ../
done

%install
rm -rf $RPM_BUILD_ROOT


for i in `find * -maxdepth 0 -type d -print`; do
	cd "$i"
	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT
	cd ../
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n sylpheed-claws-plugin-gtkhtml2_viewer
%defattr(644,root,root,755)
%doc maildir-*/ChangeLog maildir-*/README
%attr(755,root,root) %{_plugins_dir}/gtkhtml2_viewer.so
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/gtkhtml2_viewer.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/gtkhtml2_viewer.mo

%files -n sylpheed-claws-plugin-maildir
%defattr(644,root,root,755)
%doc maildir-*/ChangeLog maildir-*/README
%attr(755,root,root) %{_plugins_dir}/maildir.so

%files -n sylpheed-claws-plugin-smime
%defattr(644,root,root,755)
%doc smime-*/ChangeLog smime-*/README
%attr(755,root,root) %{_plugins_dir}/smime.so

%files -n sylpheed-claws-plugin-others
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugins_dir}/acpi_notifier.so
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/acpi_notifier.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/acpi_notifier.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/acpi_notifier.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/acpi_notifier.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/acpi_notifier.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/acpi_notifier.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/acpi_notifier.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/acpi_notifier.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/acpi_notifier.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/acpi_notifier.mo
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
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/rssyl.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/rssyl.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/rssyl.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/rssyl.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/rssyl.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/rssyl.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/rssyl.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/rssyl.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/rssyl.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/rssyl.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/rssyl.mo
%attr(755,root,root) %{_plugins_dir}/synce_plugin.so
%attr(755,root,root) %{_plugins_dir}/vcalendar.so
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/vcalendar.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/vcalendar.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/vcalendar.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/vcalendar.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/vcalendar.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/vcalendar.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/vcalendar.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/vcalendar.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/vcalendar.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/vcalendar.mo
