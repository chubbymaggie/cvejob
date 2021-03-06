"""Global configuration for the project."""

import os


class DefaultConfig(object):
    """Default configuration holder."""

    # ecosystem/language to work with
    ecosystem = 'python'

    # max age of a CVE, in days; older CVEs will be ignored.
    # 0 = disable this option and process all CVEs.
    cve_age = 0

    # location of the default NVD JSON feeds
    feed_dir = 'nvd-data/'

    # path to the default NVD JSON feed
    feed_names = None

    # range of CVES to process, all other CVEs will be ignored
    date_range = None

    # ID of a CVE to process, all other CVEs will be ignored
    cve_id = None

    # package name, requires also cve_id to be set
    package_name = None

    # location of the cpe2pkg Jar file
    cpe2pkg_path = 'cpe2pkg.jar'

    # directory where to find files containing package names
    pkgfile_dir = 'data/'

    # whether or not to use nvd-toolkit
    use_nvdtoolkit = False

    # directory where to find pretrained classifier for the nvd-toolkit
    nvdtoolkit_export_dir = 'export/'


class RuntimeConfig(object):
    """Runtime configuration holder."""

    def __init__(self):
        """Initialize Constructor."""
        self._config = DefaultConfig()

        ecosystem = os.environ.get('CVEJOB_ECOSYSTEM')
        if ecosystem is not None:
            self._config.ecosystem = ecosystem

        cve_age = os.environ.get('CVEJOB_CVE_AGE')
        if cve_age is not None:
            self._config.cve_age = int(cve_age)

        feed_dir = os.environ.get('CVEJOB_FEED_DIR')
        if feed_dir is not None:
            self._config.feed_dir = feed_dir

        feed_names = os.environ.get('CVEJOB_FEED_NAMES')
        if feed_names is not None:
            self._config.feed_names = feed_names.split(',')

        date_range = os.environ.get('CVEJOB_DATE_RANGE')
        if date_range is not None:
            self._config.date_range = date_range

        cve_id = os.environ.get('CVEJOB_CVE_ID')
        if cve_id is not None:
            self._config.cve_id = cve_id

        package_name = os.environ.get('CVEJOB_PACKAGE_NAME')
        if package_name is not None:
            self._config.package_name = package_name

        cpe2pkg_path = os.environ.get('CVEJOB_CPE2PKG_PATH')
        if cpe2pkg_path is not None:
            self._config.cpe2pkg_path = cpe2pkg_path

        pkgfile_dir = os.environ.get('CVEJOB_PKGFILE_DIR')
        if pkgfile_dir is not None:
            self._config.pkgfile_dir = pkgfile_dir

        use_nvdtoolkit = os.environ.get('CVEJOB_USE_NVD_TOOLKIT')
        if use_nvdtoolkit is not None:
            self._config.use_nvdtoolkit = use_nvdtoolkit.lower() in ('true', '1', 'yes')

        nvdtoolkit_export_dir = os.environ.get('CVEJOB_NVD_TOOLKIT_EXPORT_DIR')
        if nvdtoolkit_export_dir is not None:
            self._config.nvdtoolkit_export_dir = nvdtoolkit_export_dir

    def __getattr__(self, item):
        """Get attribute."""
        return getattr(self._config, item)


Config = RuntimeConfig()
