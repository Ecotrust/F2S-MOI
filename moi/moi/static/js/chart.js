$( window ).load(function() {
    if ( $('.template-datapage').length)  {
        $.each(vizArray, function(index, val) {
            createChart(val)
        });

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
                ['#ba2226', '#c08477', '#e6d1ca'],
                //education
                ['#185377', '#98a2b8', '#d1d4de'],
                //health
                ['#f6ab1b', '#fbca7a', '#feeacd'],
                //economy
                ['#83b841', '#b2ce87', '#e9f0dc']
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
                    chart.tooltipContent(function(key, y, e, graph) {
                        var x = String(key);
                        var y =  String(y.slice(0,2));
                        tooltip_str = '<center><b>'+y+'%</b></center>' + x;
                        return tooltip_str;
                    });

                    chart.showLegend(false)
                        .showLabels(false)
                        .donut(true)
                        .donutRatio(0.35)
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
                        .margin({top: 30, right: 50, bottom: 50, left: 200});

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
    }
});
