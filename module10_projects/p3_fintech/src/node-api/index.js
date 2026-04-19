const http = require('http');

console.log("💎 Fintech Wallet API Starting...");

const server = http.createServer((req, res) => {
    console.log("💰 Wallet Sync Request Received");
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ 
        balance: 1.245, 
        currency: "BTC",
        status: "synced with blockchain"
    }));
});

server.listen(3000, '0.0.0.0', () => {
    console.log("✅ Wallet API listening on port 3000");
});
