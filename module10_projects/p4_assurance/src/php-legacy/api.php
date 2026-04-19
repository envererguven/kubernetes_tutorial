<?php
echo "🏛️ Legacy Claims Portal API Starting...\n";

while (true) {
    echo "[" . date("H:i:s") . "] Fetching legacy policy records from Redis cache...\n";
    usleep(5000000); // 5 seconds
    echo "[" . date("H:i:s") . "] Records synchronized. Ready for workflow engine.\n";
    usleep(15000000); // 15 seconds
}
?>
