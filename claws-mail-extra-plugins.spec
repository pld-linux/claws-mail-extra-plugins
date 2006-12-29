Summary:	Plugins for Claws-Mail (metapackage)
Summary(pl):	Wtyczki dla Claws-Mail (metapakiet)
Name:		claws-mail-extra-plugins
Version:	2.6.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	a8e0639de0becad065cac90dc3ae5e8a
URL:		http://www.claws-mail.net/plugins.php
BuildRequires:	curl-devel
BuildRequires:	libgtkhtml-devel
BuildRequires:	perl-devel
BuildRequires:	claws-mail-devel >= 2.5.0
BuildRequires:	synce-librapi2-devel
BuildRequires:	synce-libsynce-devel
Requires:	claws-mail >= 2.5.0
Requires:	claws-mail-plugin-acpi_notifier = %{version}-%{release}
Requires:	claws-mail-plugin-att_remover = %{version}-%{release}
Requires:	claws-mail-plugin-cachesaver = %{version}-%{release}
Requires:	claws-mail-plugin-etpan-privacy = %{version}-%{release}
Requires:	claws-mail-plugin-fetchinfo = %{version}-%{release}
Requires:	claws-mail-plugin-gtkhtml2_viewer = %{version}-%{release}
Requires:	claws-mail-plugin-maildir = %{version}-%{release}
Requires:	claws-mail-plugin-mailmbox = %{version}-%{release}
Requires:	claws-mail-plugin-newmail = %{version}-%{release}
Requires:	claws-mail-plugin-notification = %{version}-%{release}
Requires:	claws-mail-plugin-perl = %{version}-%{release}
Requires:	claws-mail-plugin-rssyl = %{version}-%{release}
Requires:	claws-mail-plugin-smime = %{version}-%{release}
Requires:	claws-mail-plugin-synce = %{version}-%{release}
Requires:	claws-mail-plugin-vcalendar = %{version}-%{release}
Obsoletes:	claws-mail-plugin-others
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugins_dir	%{_libdir}/claws-mail/plugins

%description
Plugins for Claws-Mail (metapackage).

%description -l pl
Wtyczki dla Claws-Mail (metapakiet).

%package -n claws-mail-plugin-acpi_notifier
Summary:	acpi_notifier plugin for Claws-Mail
Summary(pl):	Wtyczka acpi_notifier dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-acpi_notifier
This plugin enables mail notification via LEDs on some laptops.

%description -n claws-mail-plugin-acpi_notifier -l pl
Ta wtyczka umo¿liwia w niektórych laptopach powiadamianie o nowej
poczcie poprzez diody LED.

%package -n claws-mail-plugin-att_remover
Summary:	att_remover plugin for Claws-Mail
Summary(pl):	Wtyczka att_remover dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-att_remover
This plugin lets you remove attachments from emails.

%description -n claws-mail-plugin-att_remover -l pl
Ta wtyczka pozwala usuwaæ za³±czniki z poczty.

%package -n claws-mail-plugin-cachesaver
Summary:	cachesaver plugin for Claws-Mail
Summary(pl):	Wtyczka cachesaver dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-cachesaver
This plugin saves the caches every 60 seconds (or user-defined
period). It helps avoiding the loss of metadata on crashes.

%description -n claws-mail-plugin-cachesaver -l pl
Ta wtyczka zapisuje cache co 60 sekund (lub w zdefiniowanym przez
u¿ytkownika okresie). Pomaga unikn±æ utraty metadanych podczas awarii
programu.

%package -n claws-mail-plugin-etpan-privacy
Summary:	etpan-privacy plugin for Claws-Mail
Summary(pl):	Wtyczka etpan-privacy dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-etpan-privacy
This plugin handles signature verification and decryption of encrypted
messages in S/MIME, OpenPGP, and ascii-armored PGP formats.

%description -n claws-mail-plugin-etpan-privacy -l pl
Ta wtyczka obs³uguje sprawdzanie podpisów i odszyfrowywanie wiadomo¶ci
w formatach S/MIME, OpenPGP i opakowanym w ASCII (ascii-armored) PGP.

%package -n claws-mail-plugin-fetchinfo
Summary:	fetchinfo plugin for Claws-Mail
Summary(pl):	Wtyczka fetchinfo dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-fetchinfo
This plugin inserts headers containing some download information:
UIDL, Claws-Mail, account name, POP server, user ID and retrieval
time.

%description -n claws-mail-plugin-fetchinfo -l pl
Ta wtyczka wstawia nag³ówki zawieraj±ce informacje o ¶ci±ganiu: UIDL,
Claws-Mail, nazwê konta, serwer POP, identyfikator u¿ytkownika i
czas pobrania.

%package -n claws-mail-plugin-gtkhtml2_viewer
Summary:	gtkhtml2_viewer plugin for Claws-Mail
Summary(pl):	Wtyczka gtkhtml2_viewer dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-gtkhtml2_viewer
Renders HTML mail using the gtkhtml2 rendering widget.

%description -n claws-mail-plugin-gtkhtml2_viewer -l pl
Wy¶wietla pocztê w HTML-u u¿ywaj±c widgeta gtkhtml2.

%package -n claws-mail-plugin-maildir
Summary:	Maildir++ plugin for Claws-Mail
Summary(pl):	Wtyczka Maildir++ dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-maildir
The Maildir++ plugin for Claws-Mail provides direct access to
Maildir++ Mailboxes used by IMAP-Servers like Courier-IMAP, BincIMAP
or Dovecot without having all the IMAP overhead of a connection to
'localhost'.

%description -n claws-mail-plugin-maildir -l pl
Wtyczka obs³ugi Maildir++ dla Claws-Mail umo¿liwia bezpo¶redni
dostêp do skrzynek formatu Maildir++ u¿ywanych przez serwery IMAP, jak
np. Courier-IMAP, BincIMAP czy Dovecot bez narzutu zwi±zanego z
obs³ug± protoko³u IMAP przy po³±czeniu z "localhostem".

%package -n claws-mail-plugin-mailmbox
Summary:	mailMBOX plugin for Claws-Mail
Summary(pl):	Wtyczka mailMBOX dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-mailmbox
This plugin handles mailboxes in mbox format.

%description -n claws-mail-plugin-mailmbox -l pl
Ta wtyczka obs³uguje skrzynki w formacie mbox.

%package -n claws-mail-plugin-newmail
Summary:	newmail plugin for Claws-Mail
Summary(pl):	Wtyczka newmail dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-newmail
This plugin writes a msg header summary to a log file, (Default:
~/Mail/NewLog), on arrival of new mail after sorting.

%description -n claws-mail-plugin-newmail -l pl
Ta wtyczka zapisuje podsumowanie nag³ówków wiadomo¶ci do pliku loga
(domy¶lnie ~/Mail/NewLog) w czasie dostarczania nowej poczty, po
sortowaniu.

%package -n claws-mail-plugin-notification
Summary:	notification plugin for Claws-Mail
Summary(pl):	Wtyczka notification dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-notification
This plugin provides various ways to notify the user of new and unread
email.

%description -n claws-mail-plugin-notification -l pl
Ta wtyczka udostêpnia ró¿ne sposoby informowania u¿ytkownika o nowej i
nieprzeczytanej poczcie.

%package -n claws-mail-plugin-perl
Summary:	perl plugin for Claws-Mail
Summary(pl):	Wtyczka perl dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-perl
This plugin is intended to extend the filtering possibilities of
Claws-Mail. It provides a Perl interface to Claws-Mail
filtering mechanism, allowing the use of full Perl power in email
filters.

%description -n claws-mail-plugin-perl -l pl
Ta wtyczka ma na celu rozszerzenie mo¿liwo¶ci filtrowania
Sylpheeda-Claws. Udostêpnia perlowy interfejs do mechanizmów
filtrowania Sylpheeda-Claws, pozwalaj±c na u¿ycie pe³nej mocy Perla w
filtrach wiadomo¶ci.

%package -n claws-mail-plugin-rssyl
Summary:	RSSyl plugin for Claws-Mail
Summary(pl):	Wtyczka RSSyl dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-rssyl
This plugin allows you to read your favorite newsfeeds in
Claws-Mail. RSS 1.0, 2.0 and Atom feeds are currently supported.

%description -n claws-mail-plugin-rssyl -l pl
Ta wtyczka pozwala na czytanie ulubionych nowinek w Sylpheedzie-Claws.
Aktualnie obs³ugiwane s± formaty RSS 1.0, 2.0 i Atom.

%package -n claws-mail-plugin-smime
Summary:	S/MIME plugin for Claws-Mail
Summary(pl):	Wtyczka S/MIME dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-smime
This plugin handles S/MIME signed and/or encrypted mails. You can
decrypt mails, verify signatures or sign and encrypt your own mails.

%description -n claws-mail-plugin-smime -l pl
Ta wtyczka obs³uguje podpisan± i/lub zaszyfrowan± pocztê S/MIME.
Pozwala rozszyfrowywaæ, weryfikowaæ lub podpisywaæ i szyfrowaæ w³asn±
pocztê.

%package -n claws-mail-plugin-synce
Summary:	SynCE plugin for Claws-Mail
Summary(pl):	Wtyczka SynCE dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-synce
This plugin assists in keeping the addressbook of a Windows CE device
in sync with Claws-Mail addressbook, with respect to email
addresses.

%description -n claws-mail-plugin-synce -l pl
Ta wtyczka pomaga w utrzymywaniu ksi±¿ki adresowej urz±dzeñ z Windows
CE w synchronizacji z ksi±¿k± adresow± Sylpheeda-Claws, uwzglêdniaj±c
adresy pocztowe.

%package -n claws-mail-plugin-vcalendar
Summary:	vCalendar plugin for Claws-Mail
Summary(pl):	Wtyczka vCalendar dla Claws-Mail
Group:		X11/Applications/Networking
Requires:	claws-mail >= 2.5.0

%description -n claws-mail-plugin-vcalendar
This plugin enables vCalendar message handling like that produced by
Evolution or Outlook and handles webCal subscriptions.

%description -n claws-mail-plugin-vcalendar -l pl
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

%files -n claws-mail-plugin-acpi_notifier -f acpi_notifier.lang
%defattr(644,root,root,755)
%doc acpi_notifier-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/acpi_notifier.so

%files -n claws-mail-plugin-att_remover
%defattr(644,root,root,755)
%doc att_remover-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/att_remover.so

%files -n claws-mail-plugin-cachesaver
%defattr(644,root,root,755)
%doc cachesaver-*/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_plugins_dir}/cachesaver.so

%files -n claws-mail-plugin-etpan-privacy
%defattr(644,root,root,755)
%doc etpan-privacy-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/etpan-privacy.so

%files -n claws-mail-plugin-fetchinfo
%defattr(644,root,root,755)
%doc fetchinfo-plugin-*/{ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/fetchinfo_plugin.so

%files -n claws-mail-plugin-gtkhtml2_viewer -f gtkhtml2_viewer.lang
%defattr(644,root,root,755)
%doc gtkhtml2_viewer-*/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_plugins_dir}/gtkhtml2_viewer.so

%files -n claws-mail-plugin-maildir
%defattr(644,root,root,755)
%doc maildir-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/maildir.so

%files -n claws-mail-plugin-mailmbox
%defattr(644,root,root,755)
%doc mailmbox-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/mailmbox.so

%files -n claws-mail-plugin-newmail
%defattr(644,root,root,755)
%doc newmail-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/newmail.so

%files -n claws-mail-plugin-notification
%defattr(644,root,root,755)
%doc notification_plugin-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/notification_plugin.so

%files -n claws-mail-plugin-perl
%defattr(644,root,root,755)
%doc perl_plugin-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/perl_plugin.so

%files -n claws-mail-plugin-rssyl -f rssyl.lang
%defattr(644,root,root,755)
%doc rssyl-*/{AUTHORS,ChangeLog,TODO}
%attr(755,root,root) %{_plugins_dir}/rssyl.so

%files -n claws-mail-plugin-smime
%defattr(644,root,root,755)
%doc smime-*/{ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/smime.so

%files -n claws-mail-plugin-synce
%defattr(644,root,root,755)
%doc synce_plugin-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/synce_plugin.so

%files -n claws-mail-plugin-vcalendar -f vcalendar.lang
%defattr(644,root,root,755)
%doc vcalendar-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/vcalendar.so
