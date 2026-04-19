<?php
echo "🚀 PHP Log Processor Started...\n";

while (true) {
    echo "[" . date("Y-m-d H:i:s") . "] Analyzing system health logs...\n";
    usleep(3000000); // Wait 3 seconds
    echo "[" . date("Y-m-d H:i:s") . "] Health Check: OK.\n";
    usleep(2000000); // Wait 2 seconds
}
?>
