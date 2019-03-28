Summary: qemu-dm device model
Name: xen-device-model
Version: 0.10.2.xs
Release: 3.0.4%{dist}
License: GPL
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/qemu-trad/archive?at=8b4834ee1202852ed83a9fc61268c65fb6961ea7&prefix=%{name}-%{version}&format=tar.gz#/%{name}-%{version}.tar.gz
Patch0: out-of-xen-build.patch
Patch1: xenserver-build-tweaks.patch
Patch2: coverity-model.patch
Patch3: builder-makefiles.patch
Patch4: revert-6e208097272.patch
Patch5: fix-vga-debug-prints.patch
Patch6: xsa211-qemut.patch
Patch7: fix-cdrom-eject.patch
Patch8: fix-pasprintf.patch
Patch9: less-leaky-xenstore-handling.patch
Patch10: fix-migrate-from-Boston-thru-Clearwater.patch
Patch11: revert-f95d202ed6444dacb15fbea4dee185eb0e048d9a.patch
Patch12: revert-7440-f37b6dee9f16.patch
Patch13: qemu-753b4053311ff1437d99726970b1e7e6bf38249b.patch
Patch14: qemu-6baebed7698a37a0ac5168faf26023426b0ac940.patch
Patch15: qemu-c522d0e2dee3774884a731691a702126901a1a88.patch
Patch16: qemu-3cded5400925452fcd1adca9109a5d30a92b4dac.patch
Patch17: qemu-0fc8e0ec7f42fb79763b875edea2f50c0691c1f4.patch
Patch18: qemu-bee1b01083b6adcf580fa30e65a2e59e7231af31.patch
Patch19: qemu-89ee676eadde78677addb74ef8f356757f6f6c0a.patch
Patch20: qemu-24cf0a6e36402f3bbab1d7317de6c4d511c832e1.patch
Patch21: qemu-afd3216027e3b28b0e180ac99d87e981d169b91c.patch
Patch22: qemu-198a0039c5fca224a77e9761e2350dd9cc102ad0.patch
Patch23: qemu-f22f5b077c164b864dae9776f63ed9e48a973fb6.patch
Patch24: vnc_timer.patch
Patch25: vnc_single_server_surf.patch
Patch26: vnc_dynamic_timer.patch
Patch27: vnc_update_policy.patch
Patch28: vnc_refresh_vnc_disconnect.patch
Patch29: qemu-5d95ac5b6475c3b6b0e36b5f04de49bba88b3e59.patch
Patch30: qemu-83755c173f4608764e3ee92428247d1c5e962e6a.patch
Patch31: CA-248714-Don-t-fail-to-start-if-no-IPv4-address-is-.patch
Patch32: xsa-126-workaround-sbr-side-effect.patch
Patch33: fix_savevm_v1_compatibility.patch
Patch34: savevm_george_compatibility.patch
Patch35: sanify-usb-controller-setup.patch
Patch36: monitor_on_xenstore.patch
Patch37: cdrom_insert_open_flags.patch
Patch38: fix_rtl_saverestore.patch
Patch39: vga-clear-fb-on-switch-to-graphic.patch
Patch40: unplug-version-2.patch
Patch41: CA-55725-retry-after-listen-fail.patch
Patch42: CP-3235.patch
Patch43: product-nr-3-blacklist.patch
Patch44: product-nr-4-blacklist.patch
Patch45: product-nr-1-blacklist.patch
Patch46: 0001-vga-map-VRAM-when-BAR-is-updated-enabled.patch
Patch47: fix-ide-cancel.patch
Patch48: qemu-3.4-fdc.patch
Patch49: hvm-late-unpause.patch
Patch50: xen-platform-scsi-controller.patch
Patch51: xenstore_set_device_locked.patch
Patch52: close-and-flush-disconnected-emulated-devices.patch
Patch53: qemu-logconsole-to-file.patch
Patch54: qemu-dont-probe-disk-format.patch
Patch55: qemu-force-lba-geometry.patch
Patch56: qemu-fix-tap-open-race-CA-8496.patch
Patch57: CA-8472.patch
Patch58: CA-10912-silence-parallel-msg.patch
Patch59: qemu-enforce-read-only-CA-12833.patch
Patch60: acpi-wake-timer.patch
Patch61: qemu-keymap.patch
Patch62: vnc_clipboard.patch
Patch63: vnclisten.patch
Patch64: vnc-port.patch
Patch65: vnc_scan_code.patch
Patch66: vnc_xencenter_no_copyrect.patch
Patch67: large_resolution.patch
Patch68: cavium_n3_passthru.patch
Patch69: enable_cirrus_irq.patch
Patch70: xenstore-exit-on-domain-destruction.patch
Patch71: set_timeoffset.patch
Patch72: qemu-use-backdev.patch
Patch73: move-disable-pf-key.patch
Patch74: CA-32196-disable-fw-cfg.patch
Patch75: abort-on-bad-loadvm.patch
Patch76: savevm_dummy_handler_for_pcislots.patch
Patch77: fix-vnc-overflow.patch
Patch78: fix_term_handling_if_paused.patch
Patch79: vnc_checks.patch
Patch80: CA-86932-disable-console-for-parallel-port.patch
Patch81: CA-87350-fix-qemu-crash-on-snapshot.patch
Patch82: constant_devfn_for_nic.patch
Patch83: evtchn_io_old_xen.patch
Patch84: less_xs_connection.patch
Patch85: XOP-403-usb-blue-fix.patch
Patch86: CA-123830-reenable-O_DIRECT.patch
Patch87: CA-127361.patch
Patch88: vgpu.patch
Patch89: vgpu_migrate.patch
Patch90: fixed-devfn.patch
Patch91: Xen-vm-kernel-crash-in-get_free_entries-workaround.patch
Patch92: vnc-dynamically-alloc-dirty-buffers.patch
Patch93: syslog_support.patch
Patch94: name2keysym_constant.patch
Patch95: ioport_memory.patch
Patch96: zlib_leak.patch
Patch97: dynamic_vnc.patch
Patch98: unselect_console.patch
Patch99: vga_const.patch
Patch100: no_icount.patch
Patch101: pci_emulation_size.patch
Patch102: main_loop.patch
Patch103: cache_get_clock.patch
Patch104: usb_timer.patch
Patch105: vnc_limit.patch
Patch106: vnc_buffer_mmap.patch
Patch107: fix-option-rom-mapping.patch
Patch108: dirty.patch
Patch109: depriv_qemu.patch
Patch110: notify.patch
Patch111: CA-147808-vnc.patch
Patch112: CA-156663-ioperms.patch
Patch113: 0001-vnc-handle-guest-ds-with-strange-width.patch
Patch114: 0002-vga-fix-invalid-memory-accesses-with-bad-register-state.patch
Patch115: initialize-vga-vbe_LFB-regs-at-init.patch
Patch116: intel-gvt-g-initial-backport.patch
Patch117: intel-gvt-g-set-default-monitor-config.patch
Patch118: intel-gvt-g-add-vnc-console-support.patch
Patch119: intel-gvt-g-use-bitblt-for-vnc-console.patch
Patch120: intel-gvt-g-add-extra-pixel-format-support-in-vnc-console.patch
Patch121: intel-gvt-g-add-skylake-blitter-support.patch
Patch122: intel-gvt-g-rework-vnc-console-code
Patch123: intel-gvt-g-vnc-full-update.patch
Patch124: intel-gvt-g-CA-213234.patch
Patch125: intel-gvt-g-add-vgt_cap-parameter.patch
Patch126: intel-gvt-g-temporary-remove-dependency-on-xenserver-libdrm.patch
Patch127: igd_passthrough.patch
Patch128: CP-12149-xen-pvdriver.patch
Patch129: 0001-Add-64-bit-support-to-QEMU.patch
Patch130: limit-igd-passthrough-bar-to-512MB.patch
Patch131: amd-pci-command-register-intercept.patch
Patch132: amd-fd-handler-changes.patch
Patch133: amd-mxgpu-security.patch
Patch134: enable-pt-logging.patch
Patch135: vnc_setdata.patch
Patch136: 0001-CA-264441-hw-cirrus-make-alignment-checks-more-rigor.patch
Patch137: msi-fix.patch
Patch138: Add-support-for-fixed-newstyle-nbd.patch
Patch139: remove_support_for_pv_qdisk.patch
Patch140: remove_support_for_qdisk_on_fv_machine.patch
Patch141: increase_nbd_client_block_size_to_4096.patch
Patch142: CP-28132_change_nbd_filename
BuildRequires: zlib-devel, xen-libs-devel, xen-dom0-libs-devel, pciutils-devel, libpciaccess-devel, check-devel, libdrm-devel
BuildRequires: ncurses-devel
Requires(pre): shadow-utils
Requires: libdrm
Provides: qemu-xen(syslog) = 1

%description
This package contains qemu-dm, the Xen device model.

%prep
%autosetup -p1

%build
./xen-setup --disable-opengl --disable-vnc-tls --disable-blobs --disable-sdl --enable-werror
%{?cov_wrap} %{__make}
%{__make} unittests

%install
rm -rf %{buildroot}
%{?cov_wrap} %{__make} install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/var/xen/qemu

# CA-157601 - Leave Qemu where xenops expects to find it until qemu-dm-wrapper can be fixed
mkdir -p %{buildroot}%{_libdir}/xen/bin/
ln %{buildroot}%{_libexecdir}/xen/bin/qemu-dm %{buildroot}%{_libdir}/xen/bin/qemu-dm

%pre
/usr/bin/getent passwd qemu >/dev/null 2>&1 || /usr/sbin/useradd \
    -M -U -r \
    -s /sbin/nologin \
    -d / \
    qemu >/dev/null 2>&1 || :
/usr/bin/getent passwd qemu_base >/dev/null 2>&1 || /usr/sbin/useradd \
    -M -U -r \
    -s /sbin/nologin \
    -d / \
    -u 65535 \
    qemu_base >/dev/null 2>&1 || :

%files
%doc COPYING COPYING.LIB LICENSE MAINTAINERS README
%{_libexecdir}/xen/bin/qemu-dm
# CA-157601 - Leave Qemu where xenops expects to find it until qemu-dm-wrapper can be fixed
%{_libdir}/xen/bin/qemu-dm
%{_datadir}/xen/qemu/keymaps
%exclude /etc/xen/scripts/qemu-ifup
%dir /var/xen/qemu

%changelog
* Tue Jul 03 2018 Simon Rowe <simon.rowe@citrix.com> - 0.10.2.xs-3.0.4
- CP-28132: skip :exportname=... from end of nbd filename

* Mon Jun 25 2018 Simon Rowe <simon.rowe@citrix.com> - 0.10.2.xs-3.0.3
- CA-290936: Fix vgpu migration by backporting shmem IPC used in QEMU (upstream) with vgpu.

* Wed Mar 28 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.10.2.xs-3.0.1
- CP-27303: Change QEMU vGPU communication with DEMU to UNIX fifo

* Thu Oct 12 2017 Simon Rowe <simon.rowe@citrix.com> - 0.10.2.xs-2.0.11
- Fix MSI/MSI-X mask initialization

* Wed Sep 20 2017 Simon Rowe <simon.rowe@citrix.com> - 0.10.2.xs-2.0.10
- CA-264441 hw/cirrus: make alignment checks more rigorous in ROPs

