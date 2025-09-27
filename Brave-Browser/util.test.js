const fs = require('fs')

jest.mock('fs', () => ({
  existsSync: jest.fn(),
}));

jest.mock('./package.json', () => mockPackageJson, { virtual: true });

const mockPackageJson = {
  name: 'test-app',
  config: {
    projects: {
      'brave-core': {
        dir: 'src/brave',
        repository: {
          url: 'https://github.com/brave/brave-core.git'
        }
      }
    }
  }
};

describe('Comparação entre funções util.js e utilOptmized.js', () => {
  let getNPMConfigFromPackageJson
  let getNPMConfigFromPackageJsonOptmized

   
  beforeEach(() => {
    process.env['npm_package_json'] = './package.json';
    fs.existsSync.mockReturnValue(true);

    getNPMConfigFromPackageJson = require('./util').getNPMConfigFromPackageJson
    getNPMConfigFromPackageJsonOptmized = require('./utilOptmized').getNPMConfigFromPackageJsonOptmized
  });

  test('Ambas funções retornam o mesmo valor para caminho válido', () => {
    const pathArr = ['projects', 'brave-core', 'dir']

    const val1 = getNPMConfigFromPackageJson(pathArr)
    const val2 = getNPMConfigFromPackageJsonOptmized(pathArr)

    expect(val1).toEqual(val2)
    expect(val1).toBe('src/brave')
  })

  test('Ambas funções retornam undefined para caminho inválido', () => {
    const pathArr = ['projects', 'inexistente', 'dir']

    const val1 = getNPMConfigFromPackageJson(pathArr)
    const val2 = getNPMConfigFromPackageJsonOptmized(pathArr)

    expect(val1).toBeUndefined()
    expect(val2).toBeUndefined()
  })

  test('Função otimizada usa cache se chamada novamente com mesmo path', () => {
    const pathArr = ['projects', 'brave-core', 'dir']

    const val1 = getNPMConfigFromPackageJsonOptmized(pathArr)
    const val2 = getNPMConfigFromPackageJsonOptmized(pathArr)

    expect(val2).toEqual(val1)
    expect(typeof val2 === 'string').toBeTruthy()
  })
})
