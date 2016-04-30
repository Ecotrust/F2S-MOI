$( window ).load(function() {
    if ( $('.template-datapage').length)  {
        $.each(districtArray, function(index, val) {
            generateMap(val);
        });

        function generateMap(val) {
            var id = val.id,
                tool = "div.tooltip-"+id,
                elm = ".viz-"+id+" svg";

            var svg = d3.select(elm)
                .attr("preserveAspectRatio", "xMinYMin meet")
                .attr("viewBox", "0 0 950 525")
                .classed("svg-content-responsive", true);

            var tooltip = d3.select(tool);


            d3.json("/static/js/school_district_topo.json", function(error, or) {
                var colorArrays = [
                    //environment
                    '#ba2226',
                    //education
                    '#185377',
                    //health
                    '#f6ab1b',
                    //economy
                    '#83b841'
                ];

                function sectorColor(url) {
                    switch(url) {
                        case '/environment/':
                            sector = colorArrays[0];
                            break;
                        case '/education/':
                            sector = colorArrays[1];
                            break;
                        case '/health/':
                            sector = colorArrays[2];
                            break;
                        case '/economy/':
                            sector = colorArrays[3];
                            break;
                    }
                    return sector
                }

                var districts = topojson.feature(or, or.objects.school_district_geo).features,
                    ids = val.data_values;

                var projection = d3.geo.mercator()
                    .center([-120.6, 44.5])
                    .scale(4000)

                var path = d3.geo.path()
                    .projection(projection)

                svg.append("g")
                    .attr("class", "school_district_geo")
                    .selectAll("path")
                        .data(districts)
                        .enter()
                        .append("path")
                        .attr("d", path)

                        .style("fill", function(d) {
                            if (ids.indexOf(d.properties.ET_UID) > -1) { return sectorColor(dataSlug) }
                        })

                        .on('mouseover', function(d) {
                            d3.select(this).classed('hover', true)

                            tooltip
                                .style('visibility', 'visible')
                                .html(d.properties.SCHOOL_DIS);
                        })

                        .on('mousemove', function() {
                            tooltip
                                .style('left',(d3.event.pageX - 45) + 'px')
                                .style('top', (d3.event.pageY - 40) + 'px')
                        })

                        .on('mouseout', function() {
                            tooltip.style('visibility', 'hidden');
                            d3.select(this).classed('hover', false)
                        });
            });
        }
    }
});
