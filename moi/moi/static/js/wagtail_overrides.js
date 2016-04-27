$(function() {
/* data viz UI toggling */

    var $dropdown = $('#id_related_data-0-data_viz_type'),
        $xLabel = $('#id_related_data-0-x_axis_label'),
        $yLabel = $('#id_related_data-0-y_axis_label'),
        $dataLabels = $('#id_related_data-0-data_labels'),
        $urlField = $('#id_related_data-0-url');

    function findAncestors(elm){
        return elm.parent().parent().parent()
    }

    function toggleFields(){
        var $val = $dropdown.find(":selected").val();
        if ($val !== 'link') {
            findAncestors($urlField).hide();
        } else {
            findAncestors($urlField).show();
        }

        if ($val !== 'bar') {
            findAncestors($xLabel).hide();
            findAncestors($yLabel).hide();
            if ($val !== 'pie') {
                findAncestors($dataLabels).hide();
            } else {
                findAncestors($dataLabels).show();
            }
        } else {
            findAncestors($xLabel).show();
            findAncestors($yLabel).show();
        }
    }

    $dropdown.change(function() {
        toggleFields();
    })

    toggleFields();
});