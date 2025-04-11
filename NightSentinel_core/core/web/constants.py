from groom_lake.core.web.exports import _jsonify, csvify, xmlify, listify, xlsxify, proxify
from groom_lake.core.web.reports import xlsx, pushpin

EXPORTS = {
    'json': _jsonify,
    'xml': xmlify,
    'csv': csvify,
    'list': listify,
    'xlsx': xlsxify,
    'proxy': proxify,
}

REPORTS = {
    'xlsx': xlsx,
    'pushpin': pushpin,
}
