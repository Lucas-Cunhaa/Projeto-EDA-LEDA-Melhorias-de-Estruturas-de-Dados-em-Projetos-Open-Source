process.env.npm_package_json = './package.json';
process.env.PROJECT_PATH = './package.json';

const utils = require('./util.js');
const utilsOptmized = require('./utilOptmized.js')
// --- Testes ---

let result1 = utils.getNPMConfigFromPackageJson(['projects', 'brave-core', 'repository', 'url']);
console.log("Resultado para ['projects', 'brave-core', 'repository', 'url']:", result1);

let result2 = utils.getNPMConfigFromPackageJson(['database', 'user']);
console.log("Resultado para ['database', 'user']:", result2);

let result4 = utilsOptmized.getNPMConfigFromPackageJsonOptmized(['projects', 'brave-core', 'repository', 'url']);
console.log("Resultado para ['projects', 'brave-core', 'repository', 'url']:", result4);

let result5 = utilsOptmized.getNPMConfigFromPackageJsonOptmized(['database', 'user']);
console.log("Resultado para ['database', 'user']:", result5);