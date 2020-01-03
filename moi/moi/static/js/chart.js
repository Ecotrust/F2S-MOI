$( window ).load(function() {
    if ( $('.template-datapage').length && typeof vizArray !== 'undefined')  {

        function sectorColor(dataSlug, array) {
            switch(dataSlug) {
                case '/environment/':
                    sector = array[0];
                    break;
                case '/education/':
                    sector = array[1];
                    break;
                case '/health/':
                    sector = array[2];
                    break;
                case '/economy/':
                    sector = array[3];
                    break;
            }
            return sector
        }

        function createChart(val) {
            var pieColorArrays = [
                //environment
                ['#ba2227', '#cdaa7d', '#e6d1ca'],
                //education
                ['#185377', '#E82128', '#d1d4de'],
                //health
                // ['#f6ab1b', '#81B79C', '#feeacd'],
                ['#f6ab1b', '#523E18', '#B89681', '#57C1A6', '#8DEBB9', '#185233', '#87B881', '#B657C1', '#C88DEB'],
                //economy
                ['#83b841', '#28A8E0', '#e9f0dc']
            ];

            var multiBarHorizontalColorArrays = [
                //environment
                ['#ba2226', '#ae6054', '#c08477', '#d6aea3', '#e6d1ca'],
                //education
                ['#185377', '#5e7493', '#98a2b8', '#aeb5c6', '#d1d4de'],
                //health
                ['#f6ab1b', '#f9ba43', '#fbca7a', '#fddaa2', '#feeacd'],
                //economy
                ['#83b841', '#9bc261', '#b2ce87', '#cbdcab', '#e9f0dc']
            ];

            var data = [{"values":  val.chartdata }],
                id = val.chartcontainer,
                elm = '#'+id,
                type = val.charttype;

            if (type === 'pie') {
                var datum = data[0].values,
                    circleSelect = elm+' .fa-circle',
                    array = pieColorArrays;

                d3.selectAll(circleSelect).each(function(d,i) {
                    d3.select(this).style('color', sectorColor(dataSlug, array)[i])
                })
            } else {
                var datum = data,
                    array = multiBarHorizontalColorArrays;
            }

            nv.addGraph(function() {
                if (type == 'pie') {
                    var chart = nv.models.pieChart();
                } else {
                    var chart = nv.models.multiBarHorizontalChart();
                }

                chart.x(function(d) { return d.label })
                    .y(function(d) { return d.value });

                //pie-donut
                if (type === 'pie') {
                    chart.showLegend(false)
                        .tooltips(false)
                        .donut(true)
                        .donutRatio(0.35)
                        .labelThreshold(.10)
                        .labelType("percent")
                        .growOnHover(false)
                        .color(sectorColor(dataSlug, array));

                //barchart
                } else {
                    chart.stacked(false)
                        .tooltips(false)
                        .showControls(false)
                        .showLegend(false)
                        .showValues(true)
                        .valueFormat(d3.format('.2'))
                        .barColor(sectorColor(dataSlug, array))

                    if (window.outerWidth <= 450) {
                        chart.margin({top: 30, right: 20, bottom: 50, left: 150});
                    } else {
                        chart.margin({top: 30, right: 50, bottom: 50, left: 200});
                    }

                    chart.yAxis
                        .tickFormat(d3.format('.2'));
                }

                d3.select(elm+' svg')
                    .datum(datum)
                    .transition().duration(500)
                    .call(chart);

                nv.utils.windowResize(chart.update);
                return chart;
            });
        }

        $.each(vizArray, function(index, val) {
            createChart(val)
        });
    }
});
