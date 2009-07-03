Summary:	Plugins for Claws-Mail (metapackage)
Summary(pl.UTF-8):	Wtyczki dla Claws-Mail (metapakiet)
Name:		claws-mail-extra-plugins
Version:	3.7.2
Release:	2
License:	GPL v3
Group:		Applications
Source0:	http://dl.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# Source0-md5:	0bdbbf69b2420e4bbb8d0ae85f9f85d6
URL:		http://www.claws-mail.net/plugins.php
BuildRequires:	claws-mail-devel >= 3.7.0
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtk-webkit-devel
BuildRequires:	libarchive-devel
BuildRequires:	libgtkhtml-devel
BuildRequires:	libnotify-devel >= 0.4.3
BuildRequires:	libxml2-devel
BuildRequires:	libytnef-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	synce-librapi2-devel
BuildRequires:	synce-libsynce-devel
%requires_eq	claws-mail
Requires:	claws-mail-plugin-acpi_notifier = %{version}-%{release}
Requires:	claws-mail-plugin-archive = %{version}-%{release}
Requires:	claws-mail-plugin-att_remover = %{version}-%{release}
Requires:	claws-mail-plugin-attachwarner = %{version}-%{release}
Requires:	claws-mail-plugin-bsfilter = %{version}-%{release}
Requires:	claws-mail-plugin-cachesaver = %{version}-%{release}
Requires:	claws-mail-plugin-fancy = %{version}-%{release}
Requires:	claws-mail-plugin-fetchinfo = %{version}-%{release}
Requires:	claws-mail-plugin-gtkhtml2_viewer = %{version}-%{release}
Requires:	claws-mail-plugin-mailmbox = %{version}-%{release}
Requires:	claws-mail-plugin-newmail = %{version}-%{release}
Requires:	claws-mail-plugin-notification = %{version}-%{release}
Requires:	claws-mail-plugin-perl = %{version}-%{release}
Requires:	claws-mail-plugin-rssyl = %{version}-%{release}
Requires:	claws-mail-plugin-spamreport = %{version}-%{release}
Requires:	claws-mail-plugin-synce = %{version}-%{release}
Requires:	claws-mail-plugin-tnef_parse = %{version}-%{release}
Requires:	claws-mail-plugin-vcalendar = %{version}-%{release}
Provides:	sylpheed-claws-extra-plugins
Obsoletes:	claws-mail-plugin-pdf_viewer
Obsoletes:	sylpheed-claws-extra-plugins
Obsoletes:	sylpheed-claws-plugin-others
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugins_dir	%{_libdir}/claws-mail/plugins

%description
Plugins for Claws-Mail (metapackage).

%description -l pl.UTF-8
Wtyczki dla Claws-Mail (metapakiet).

%package -n claws-mail-plugin-acpi_notifier
Summary:	acpi_notifier plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka acpi_notifier dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-acpi_notifier
Obsoletes:	sylpheed-claws-plugin-acpi_notifier

%description -n claws-mail-plugin-acpi_notifier
This plugin enables mail notification via LEDs on some laptops.

%description -n claws-mail-plugin-acpi_notifier -l pl.UTF-8
Ta wtyczka umożliwia w niektórych laptopach powiadamianie o nowej
poczcie poprzez diody LED.

%package -n claws-mail-plugin-archive
Summary:	archive plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka archive dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail

%description -n claws-mail-plugin-archive
This plugin lets you archive IMAP, LOCAL and POP accounts as well as
calendar accounts.

%description -n claws-mail-plugin-archive -l pl.UTF-8
Ta wtyczka pozwala archiwizować konta IMAP, LOCAL i POP jak również
kalendarze.

%package -n claws-mail-plugin-att_remover
Summary:	att_remover plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka att_remover dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-att_remover
Obsoletes:	sylpheed-claws-plugin-att_remover

%description -n claws-mail-plugin-att_remover
This plugin lets you remove attachments from emails.

%description -n claws-mail-plugin-att_remover -l pl.UTF-8
Ta wtyczka pozwala usuwać załączniki z poczty.

%package -n claws-mail-plugin-attachwarner
Summary:	attachwarner plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka attachwarner dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail

%description -n claws-mail-plugin-attachwarner
This plugin warns when the user composes a message mentioning an
attachment in the message body, but without attaching any files to the
message.

%description -n claws-mail-plugin-attachwarner -l pl.UTF-8
Ta wtyczka ostrzega, kiedy użytkownik piszący wiadomość wspomina w
treści o załączniku, ale nie załącza żadnego pliku do wiadomości.

%package -n claws-mail-plugin-bsfilter
Summary:	bsfilter plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka bsfilter dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail

%description -n claws-mail-plugin-bsfilter
Check all messages that are received from an IMAP, LOCAL or POP
account for spam using Bsfilter.

%description -n claws-mail-plugin-bsfilter -l pl.UTF-8
Ta wtyczka sprawdza wszystkie wiadomości odebrane przez IMAP, lokalnie
bądź POP pod kątem występowania spamu przy użyciu bsfilter.

%package -n claws-mail-plugin-cachesaver
Summary:	cachesaver plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka cachesaver dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-cachesaver
Obsoletes:	sylpheed-claws-plugin-cachesaver

%description -n claws-mail-plugin-cachesaver
This plugin saves the caches every 60 seconds (or user-defined
period). It helps avoiding the loss of metadata on crashes.

%description -n claws-mail-plugin-cachesaver -l pl.UTF-8
Ta wtyczka zapisuje cache co 60 sekund (lub w zdefiniowanym przez
użytkownika okresie). Pomaga uniknąć utraty metadanych podczas awarii
programu.

%package -n claws-mail-plugin-fancy
Summary:	fancy plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka fancy dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail

%description -n claws-mail-plugin-fancy
Renders HTML e-mail using the WebKit library.

%description -n claws-mail-plugin-fancy -l pl.UTF-8
Ta wtyczka przetwarza wiadomości w formacie HTML przy użyciu
biblioteki WebKit.

%package -n claws-mail-plugin-fetchinfo
Summary:	fetchinfo plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka fetchinfo dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-fetchinfo
Obsoletes:	sylpheed-claws-plugin-fetchinfo

%description -n claws-mail-plugin-fetchinfo
This plugin inserts headers containing some download information:
UIDL, Claws-Mail, account name, POP server, user ID and retrieval
time.

%description -n claws-mail-plugin-fetchinfo -l pl.UTF-8
Ta wtyczka wstawia nagłówki zawierające informacje o ściąganiu: UIDL,
Claws-Mail, nazwę konta, serwer POP, identyfikator użytkownika i czas
pobrania.

%package -n claws-mail-plugin-gtkhtml2_viewer
Summary:	gtkhtml2_viewer plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka gtkhtml2_viewer dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-gtkhtml2_viewer
Obsoletes:	sylpheed-claws-plugin-gtkhtml2_viewer

%description -n claws-mail-plugin-gtkhtml2_viewer
Renders HTML mail using the gtkhtml2 rendering widget.

%description -n claws-mail-plugin-gtkhtml2_viewer -l pl.UTF-8
Wyświetla pocztę w HTML-u używając widgeta gtkhtml2.

%package -n claws-mail-plugin-mailmbox
Summary:	mailMBOX plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka mailMBOX dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-mailmbox
Obsoletes:	sylpheed-claws-plugin-mailmbox

%description -n claws-mail-plugin-mailmbox
This plugin handles mailboxes in mbox format.

%description -n claws-mail-plugin-mailmbox -l pl.UTF-8
Ta wtyczka obsługuje skrzynki w formacie mbox.

%package -n claws-mail-plugin-newmail
Summary:	newmail plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka newmail dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-newmail
Obsoletes:	sylpheed-claws-plugin-newmail

%description -n claws-mail-plugin-newmail
This plugin writes a msg header summary to a log file, (Default:
~/Mail/NewLog), on arrival of new mail after sorting.

%description -n claws-mail-plugin-newmail -l pl.UTF-8
Ta wtyczka zapisuje podsumowanie nagłówków wiadomości do pliku loga
(domyślnie ~/Mail/NewLog) w czasie dostarczania nowej poczty, po
sortowaniu.

%package -n claws-mail-plugin-notification
Summary:	notification plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka notification dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-notification
Obsoletes:	sylpheed-claws-plugin-notification

%description -n claws-mail-plugin-notification
This plugin provides various ways to notify the user of new and unread
email.

%description -n claws-mail-plugin-notification -l pl.UTF-8
Ta wtyczka udostępnia różne sposoby informowania użytkownika o nowej i
nieprzeczytanej poczcie.

%package -n claws-mail-plugin-perl
Summary:	perl plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka perl dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-perl
Obsoletes:	sylpheed-claws-plugin-perl

%description -n claws-mail-plugin-perl
This plugin is intended to extend the filtering possibilities of
Claws-Mail. It provides a Perl interface to Claws-Mail filtering
mechanism, allowing the use of full Perl power in email filters.

%description -n claws-mail-plugin-perl -l pl.UTF-8
Ta wtyczka ma na celu rozszerzenie możliwości filtrowania
Sylpheeda-Claws. Udostępnia perlowy interfejs do mechanizmów
filtrowania Sylpheeda-Claws, pozwalając na użycie pełnej mocy Perla w
filtrach wiadomości.

%package -n claws-mail-plugin-rssyl
Summary:	RSSyl plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka RSSyl dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-rssyl
Obsoletes:	sylpheed-claws-plugin-rssyl

%description -n claws-mail-plugin-rssyl
This plugin allows you to read your favorite newsfeeds in Claws-Mail.
RSS 1.0, 2.0 and Atom feeds are currently supported.

%description -n claws-mail-plugin-rssyl -l pl.UTF-8
Ta wtyczka pozwala na czytanie ulubionych nowinek w Sylpheedzie-Claws.
Aktualnie obsługiwane są formaty RSS 1.0, 2.0 i Atom.

%package -n claws-mail-plugin-spamreport
Summary:	SpamReport plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka SpamReport dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail

%description -n claws-mail-plugin-spamreport
This plugin allows you to upload spams to various spam reporting
places, like http://www.signal-spam.fr/ .

%package -n claws-mail-plugin-synce
Summary:	SynCE plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka SynCE dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-synce
Obsoletes:	sylpheed-claws-plugin-synce

%description -n claws-mail-plugin-synce
This plugin assists in keeping the addressbook of a Windows CE device
in sync with Claws-Mail addressbook, with respect to email addresses.

%description -n claws-mail-plugin-synce -l pl.UTF-8
Ta wtyczka pomaga w utrzymywaniu książki adresowej urządzeń z Windows
CE w synchronizacji z książką adresową Sylpheeda-Claws, uwzględniając
adresy pocztowe.

%package -n claws-mail-plugin-tnef_parse
Summary:	TNEF Parse plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka TNEF Parse dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail

%description -n claws-mail-plugin-tnef_parse
This plugin enables reading application/ms-tnef attachments.

%description -n claws-mail-plugin-tnef_parse -l pl.UTF-8
Ta wtyczka pozwala czytać załączniki typu application/ms-tnef.

%package -n claws-mail-plugin-vcalendar
Summary:	vCalendar plugin for Claws-Mail
Summary(pl.UTF-8):	Wtyczka vCalendar dla Claws-Mail
Group:		X11/Applications/Mail
%requires_eq	claws-mail
Provides:	sylpheed-claws-plugin-vcalendar
Obsoletes:	sylpheed-claws-plugin-vcalendar

%description -n claws-mail-plugin-vcalendar
This plugin enables vCalendar message handling like that produced by
Evolution or Outlook and handles webCal subscriptions.

%description -n claws-mail-plugin-vcalendar -l pl.UTF-8
Ta wtyczka pozwala na obsługę wiadomości vCalendar, takich jak te
tworzone przez Evolution czy Outlooka, a także obsługuje subskrypcje
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
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -f $RPM_BUILD_ROOT%{_plugins_dir}/*.{a,la,deps}

%find_lang acpi_notifier
%find_lang archive
%find_lang attachwarner
%find_lang bsfilter_plugin
%find_lang fancy
%find_lang gtkhtml2_viewer
%find_lang notification_plugin
%find_lang rssyl
%find_lang spam_report
%find_lang tnef_parse
%find_lang vcalendar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n claws-mail-plugin-acpi_notifier -f acpi_notifier.lang
%defattr(644,root,root,755)
%doc acpi_notifier-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/acpi_notifier.so

%files -n claws-mail-plugin-archive -f archive.lang
%defattr(644,root,root,755)
%doc archive-*/{AUTHORS,ChangeLog,NEWS,README,TODO}
%attr(755,root,root) %{_plugins_dir}/archive.so

%files -n claws-mail-plugin-att_remover
%defattr(644,root,root,755)
%doc att_remover-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/att_remover.so

%files -n claws-mail-plugin-attachwarner -f attachwarner.lang
%defattr(644,root,root,755)
%doc attachwarner-*/{AUTHORS,ChangeLog,README,TODO}
%attr(755,root,root) %{_plugins_dir}/attachwarner.so

%files -n claws-mail-plugin-bsfilter -f bsfilter_plugin.lang
%defattr(644,root,root,755)
%doc bsfilter_plugin-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/bsfilter.so

%files -n claws-mail-plugin-cachesaver
%defattr(644,root,root,755)
%doc cachesaver-*/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_plugins_dir}/cachesaver.so

%files -n claws-mail-plugin-fancy -f fancy.lang
%defattr(644,root,root,755)
%doc fancy-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/fancy.so

%files -n claws-mail-plugin-fetchinfo
%defattr(644,root,root,755)
%doc fetchinfo-plugin-*/{ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/fetchinfo_plugin.so

%files -n claws-mail-plugin-gtkhtml2_viewer -f gtkhtml2_viewer.lang
%defattr(644,root,root,755)
%doc gtkhtml2_viewer-*/{AUTHORS,ChangeLog}
%attr(755,root,root) %{_plugins_dir}/gtkhtml2_viewer.so

%files -n claws-mail-plugin-mailmbox
%defattr(644,root,root,755)
%doc mailmbox-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/mailmbox.so

%files -n claws-mail-plugin-newmail
%defattr(644,root,root,755)
%doc newmail-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/newmail.so

%files -n claws-mail-plugin-notification -f notification_plugin.lang
%defattr(644,root,root,755)
%doc notification_plugin-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/notification_plugin.so

%files -n claws-mail-plugin-perl
%defattr(644,root,root,755)
%doc perl_plugin-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/perl_plugin.so

%files -n claws-mail-plugin-rssyl -f rssyl.lang
%defattr(644,root,root,755)
%doc rssyl-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/rssyl.so

%files -n claws-mail-plugin-spamreport -f spam_report.lang
%defattr(644,root,root,755)
%doc spam_report-*/{ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/spamreport.so

%files -n claws-mail-plugin-synce
%defattr(644,root,root,755)
%doc synce_plugin-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/synce_plugin.so

%files -n claws-mail-plugin-tnef_parse -f tnef_parse.lang
%defattr(644,root,root,755)
%doc tnef_parse-*/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_plugins_dir}/tnef_parse.so

%files -n claws-mail-plugin-vcalendar -f vcalendar.lang
%defattr(644,root,root,755)
%doc vcalendar-*/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_plugins_dir}/vcalendar.so
