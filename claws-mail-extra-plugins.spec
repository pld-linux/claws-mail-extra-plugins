Summary:	Plugins for Sylpheed-Claws (metapackage)
Summary(pl):	Wtyczki dla Sylpheed-Claws (metapakiet)
Name:		sylpheed-claws-extra-plugins
Version:	2.3.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	06b53d69913ea1c96fb154fa2686606a
URL:		http://www.sylpheed-claws.net/plugins.php
BuildRequires:	curl-devel
BuildRequires:	libgtkhtml-devel
BuildRequires:	perl-devel
BuildRequires:	sylpheed-claws-devel >= 2.3.0
BuildRequires:	synce-librapi2-devel
BuildRequires:	synce-libsynce-devel
Requires:	sylpheed-claws >= 2.3.0
Requires:	sylpheed-claws-plugin-acpi_notifier = %{version}-%{release}
Requires:	sylpheed-claws-plugin-att_remover = %{version}-%{release}
Requires:	sylpheed-claws-plugin-cachesaver = %{version}-%{release}
Requires:	sylpheed-claws-plugin-etpan-privacy = %{version}-%{release}
Requires:	sylpheed-claws-plugin-fetchinfo = %{version}-%{release}
Requires:	sylpheed-claws-plugin-gtkhtml2_viewer = %{version}-%{release}
Requires:	sylpheed-claws-plugin-maildir = %{version}-%{release}
Requires:	sylpheed-claws-plugin-mailmbox = %{version}-%{release}
Requires:	sylpheed-claws-plugin-newmail = %{version}-%{release}
Requires:	sylpheed-claws-plugin-notification = %{version}-%{release}
Requires:	sylpheed-claws-plugin-perl = %{version}-%{release}
Requires:	sylpheed-claws-plugin-rssyl = %{version}-%{release}
Requires:	sylpheed-claws-plugin-smime = %{version}-%{release}
Requires:	sylpheed-claws-plugin-synce = %{version}-%{release}
Requires:	sylpheed-claws-plugin-vcalendar = %{version}-%{release}
Obsoletes:	sylpheed-claws-plugin-others
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugins_dir	%{_libdir}/sylpheed-claws/plugins

%description
Plugins for Sylpheed-Claws (metapackage).

%description -l pl
Wtyczki dla Sylpheed-Claws (metapakiet).

%package -n sylpheed-claws-plugin-acpi_notifier
Summary:	acpi_notifier plugin for Sylpheed-Claws
Summary(pl):	Wtyczka acpi_notifier dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-acpi_notifier
This plugin enables mail notification via LEDs on some laptops.

%description -n sylpheed-claws-plugin-acpi_notifier -l pl
Ta wtyczka umo¿liwia w niektórych laptopach powiadamianie o nowej
poczcie poprzez diody LED.

%package -n sylpheed-claws-plugin-att_remover
Summary:	att_remover plugin for Sylpheed-Claws
Summary(pl):	Wtyczka att_remover dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-att_remover
This plugin lets you remove attachments from emails.

%description -n sylpheed-claws-plugin-att_remover -l pl
Ta wtyczka pozwala usuwaæ za³±czniki z poczty.

%package -n sylpheed-claws-plugin-cachesaver
Summary:	cachesaver plugin for Sylpheed-Claws
Summary(pl):	Wtyczka cachesaver dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-cachesaver
This plugin saves the caches every 60 seconds (or user-defined
period). It helps avoiding the loss of metadata on crashes.

%description -n sylpheed-claws-plugin-cachesaver -l pl
Ta wtyczka zapisuje cache co 60 sekund (lub w zdefiniowanym przez
u¿ytkownika okresie). Pomaga unikn±æ utraty metadanych podczas awarii
programu.

%package -n sylpheed-claws-plugin-etpan-privacy
Summary:	etpan-privacy plugin for Sylpheed-Claws
Summary(pl):	Wtyczka etpan-privacy dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-etpan-privacy
This plugin handles signature verification and decryption of encrypted
messages in S/MIME, OpenPGP, and ascii-armored PGP formats.

%description -n sylpheed-claws-plugin-etpan-privacy -l pl
Ta wtyczka obs³uguje sprawdzanie podpisów i odszyfrowywanie wiadomo¶ci
w formatach S/MIME, OpenPGP i opakowanym w ASCII (ascii-armored) PGP.

%package -n sylpheed-claws-plugin-fetchinfo
Summary:	fetchinfo plugin for Sylpheed-Claws
Summary(pl):	Wtyczka fetchinfo dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-fetchinfo
This plugin inserts headers containing some download information:
UIDL, Sylpheed-Claws, account name, POP server, user ID and retrieval
time.

%description -n sylpheed-claws-plugin-fetchinfo -l pl
Ta wtyczka wstawia nag³ówki zawieraj±ce informacje o ¶ci±ganiu: UIDL,
Sylpheed-Claws, nazwê konta, serwer POP, identyfikator u¿ytkownika i
czas pobrania.

%package -n sylpheed-claws-plugin-gtkhtml2_viewer
Summary:	gtkhtml2_viewer plugin for Sylpheed-Claws
Summary(pl):	Wtyczka gtkhtml2_viewer dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-gtkhtml2_viewer
Renders HTML mail using the gtkhtml2 rendering widget.

%description -n sylpheed-claws-plugin-gtkhtml2_viewer -l pl
Wy¶wietla pocztê w HTML-u u¿ywaj±c widgeta gtkhtml2.

%package -n sylpheed-claws-plugin-maildir
Summary:	Maildir++ plugin for Sylpheed-Claws
Summary(pl):	Wtyczka Maildir++ dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

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

%package -n sylpheed-claws-plugin-mailmbox
Summary:	mailMBOX plugin for Sylpheed-Claws
Summary(pl):	Wtyczka mailMBOX dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-mailmbox
This plugin handles mailboxes in mbox format.

%description -n sylpheed-claws-plugin-mailmbox -l pl
Ta wtyczka obs³uguje skrzynki w formacie mbox.

%package -n sylpheed-claws-plugin-newmail
Summary:	newmail plugin for Sylpheed-Claws
Summary(pl):	Wtyczka newmail dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-newmail
This plugin writes a msg header summary to a log file, (Default:
~/Mail/NewLog), on arrival of new mail after sorting.

%description -n sylpheed-claws-plugin-newmail -l pl
Ta wtyczka zapisuje podsumowanie nag³ówków wiadomo¶ci do pliku loga
(domy¶lnie ~/Mail/NewLog) w czasie dostarczania nowej poczty, po
sortowaniu.

%package -n sylpheed-claws-plugin-notification
Summary:	notification plugin for Sylpheed-Claws
Summary(pl):	Wtyczka notification dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-notification
This plugin provides various ways to notify the user of new and unread
email.

%description -n sylpheed-claws-plugin-notification -l pl
Ta wtyczka udostêpnia ró¿ne sposoby informowania u¿ytkownika o nowej i
nieprzeczytanej poczcie.

%package -n sylpheed-claws-plugin-perl
Summary:	perl plugin for Sylpheed-Claws
Summary(pl):	Wtyczka perl dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-perl
This plugin is intended to extend the filtering possibilities of
Sylpheed-Claws. It provides a Perl interface to Sylpheed-Claws
filtering mechanism, allowing the use of full Perl power in email
filters.

%description -n sylpheed-claws-plugin-perl -l pl
Ta wtyczka ma na celu rozszerzenie mo¿liwo¶ci filtrowania
Sylpheeda-Claws. Udostêpnia perlowy interfejs do mechanizmów
filtrowania Sylpheeda-Claws, pozwalaj±c na u¿ycie pe³nej mocy Perla w
filtrach wiadomo¶ci.

%package -n sylpheed-claws-plugin-rssyl
Summary:	RSSyl plugin for Sylpheed-Claws
Summary(pl):	Wtyczka RSSyl dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-rssyl
This plugin allows you to read your favorite newsfeeds in
Sylpheed-Claws. RSS 1.0, 2.0 and Atom feeds are currently supported.

%description -n sylpheed-claws-plugin-rssyl -l pl
Ta wtyczka pozwala na czytanie ulubionych nowinek w Sylpheedzie-Claws.
Aktualnie obs³ugiwane s± formaty RSS 1.0, 2.0 i Atom.

%package -n sylpheed-claws-plugin-smime
Summary:	S/MIME plugin for Sylpheed-Claws
Summary(pl):	Wtyczka S/MIME dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-smime
This plugin handles S/MIME signed and/or encrypted mails. You can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description -n sylpheed-claws-plugin-smime -l pl
Ta wtyczka obs³uguje podpisan± i/lub zaszyfrowan± pocztê S/MIME.
Pozwala rozszyfrowywaæ, weryfikowaæ lub podpisywaæ i szyfrowaæ w³asn±
pocztê.

%package -n sylpheed-claws-plugin-synce
Summary:	SynCE plugin for Sylpheed-Claws
Summary(pl):	Wtyczka SynCE dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-synce
This plugin assists in keeping the addressbook of a Windows CE device
in sync with Sylpheed-Claws addressbook, with respect to email
addresses.

%description -n sylpheed-claws-plugin-synce -l pl
Ta wtyczka pomaga w utrzymywaniu ksi±¿ki adresowej urz±dzeñ z Windows
CE w synchronizacji z ksi±¿k± adresow± Sylpheeda-Claws, uwzglêdniaj±c
adresy pocztowe.

%package -n sylpheed-claws-plugin-vcalendar
Summary:	vCalendar plugin for Sylpheed-Claws
Summary(pl):	Wtyczka vCalendar dla Sylpheed-Claws
Group:		X11/Applications/Networking
Requires:	sylpheed-claws >= 2.3.0

%description -n sylpheed-claws-plugin-vcalendar
This plugin enables vCalendar message handling like that produced by
Evolution or Outlook and handles webCal subscriptions.

%description -n sylpheed-claws-plugin-vcalendar -l pl
Ta wtyczka pozwala na obs³ugê wiadomo¶ci vCalendar, takich jak te
tworzone przez Evolution czy Outlooka, a tak¿e obs³uguje subskrypcje
webCal.

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

rm -f $RPM_BUILD_ROOT%{_includedir}/*.h
rm -f $RPM_BUILD_ROOT%{_plugins_dir}/*.{a,la,deps}

%find_lang acpi_notifier
%find_lang gtkhtml2_viewer
%find_lang rssyl
%find_lang vcalendar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n sylpheed-claws-plugin-acpi_notifier -f acpi_notifier.lang
%defattr(644,root,root,755)
%doc acpi_notifier-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/acpi_notifier.so

%files -n sylpheed-claws-plugin-att_remover
%defattr(644,root,root,755)
%doc att_remover-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/att_remover.so

%files -n sylpheed-claws-plugin-cachesaver
%defattr(644,root,root,755)
%doc cachesaver-*/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_plugins_dir}/cachesaver.so

%files -n sylpheed-claws-plugin-etpan-privacy
%defattr(644,root,root,755)
%doc etpan-privacy-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/etpan-privacy.so

%files -n sylpheed-claws-plugin-fetchinfo
%defattr(644,root,root,755)
%doc fetchinfo-plugin-*/{ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/fetchinfo_plugin.so
%attr(755,root,root) %{_plugins_dir}/fetchinfo_plugin_gtk.so

%files -n sylpheed-claws-plugin-gtkhtml2_viewer -f gtkhtml2_viewer.lang
%defattr(644,root,root,755)
%doc gtkhtml2_viewer-*/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_plugins_dir}/gtkhtml2_viewer.so

%files -n sylpheed-claws-plugin-maildir
%defattr(644,root,root,755)
%doc maildir-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/maildir.so

%files -n sylpheed-claws-plugin-mailmbox
%defattr(644,root,root,755)
%doc mailmbox-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/mailmbox.so

%files -n sylpheed-claws-plugin-newmail
%defattr(644,root,root,755)
%doc newmail-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/newmail.so

%files -n sylpheed-claws-plugin-notification
%defattr(644,root,root,755)
%doc notification_plugin-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/notification_plugin.so

%files -n sylpheed-claws-plugin-perl
%defattr(644,root,root,755)
%doc perl_plugin-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/perl_plugin.so

%files -n sylpheed-claws-plugin-rssyl -f rssyl.lang
%defattr(644,root,root,755)
%doc rssyl-*/{AUTHORS,ChangeLog,TODO}
%attr(755,root,root) %{_plugins_dir}/rssyl.so

%files -n sylpheed-claws-plugin-smime
%defattr(644,root,root,755)
%doc smime-*/{ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/smime.so

%files -n sylpheed-claws-plugin-synce
%defattr(644,root,root,755)
%doc synce_plugin-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/synce_plugin.so

%files -n sylpheed-claws-plugin-vcalendar -f vcalendar.lang
%defattr(644,root,root,755)
%doc vcalendar-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/vcalendar.so
