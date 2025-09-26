const readline = require("readline")
const utils = require('./util.js')
const utilsOptmized = require('./utilOptmized.js')
const fs = require("fs")
const path = require("path")

const filePath = path.join(__dirname, "sample", "sizes.txt");
const readStream = fs.createReadStream(filePath, { encoding: "utf-8" });

const rl = readline.createInterface({
    input: readStream,
    crlfDelay: Infinity
});

rl.on("line", (line) => {
    const parts = line.split(/\s+/);

    parts.forEach((part) => {
        const num = parseFloat(part);
        if (!isNaN(num)) setupBenchmark(num);
    });
});

function generatePath(size) {
    const result = []
    for (let i = 0; i <= size; i++) {
        result[i] = "path" + i
        
    }
    return result
}

function generateNestedObjectByPath(path) {
    const obj = { config : {} }
    let current = obj.config

    for (let i = 0; i < path.length - 1; i++) {
        const key = path[i];
        current[key] = {};
        current = current[key];
    }
    
    current[path[path.length - 1]] = "end";

    fs.writeFileSync("package.json", JSON.stringify(obj, null, 2), "utf-8")
}

function setupBenchmark (size) {
    const path = generatePath(size)
    generateNestedObjectByPath(path)

    benchmark(utilsOptmized.getNPMConfigFromPackageJsonOptmized, "utils-optmized", path)
}

function benchmark(target, targetName, path) {
    const EXECUTION_TIME = 10000
    let time = 0
    
    for (let index = 0; index <= EXECUTION_TIME; index++) {
        const start = performance.now();
        target(path)
        const end = performance.now();
        time += (end - start) / EXECUTION_TIME
    }

    console.log(`${targetName} ${time} ${path.length-1}`) 
}
