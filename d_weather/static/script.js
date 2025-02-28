
const options = {
    key: 'FsWPqqP1ueoCxt0daZaanpGewgAYev4y', // REPLACE WITH YOUR KEY !!!
    verbose: true
};

windyInit(options, windyAPI => {
    const { overlays, broadcast } = windyAPI;
    const windMetric = overlays.wind.metric;
    console.log(windMetric);
    overlays.wind.listMetrics();
    overlays.wind.setMetric('bft');
    broadcast.on('metricChanged', (overlay, newMetric) => {
        console.log(overlay, newMetric);
    });
});
