const path = require('path')
const fs = require('fs')

jest.mock('fs') // mock do fs

describe('Comparação entre funções util.js e utilOptmized.js', () => {
  const fakePackagePath = path.join(__dirname, 'fake.package.json')
  let getNPMConfigFromPackageJson
  let getNPMConfigFromPackageJsonOptmized

  beforeEach(() => {
    jest.resetModules()
    process.env['npm_package_json'] = fakePackagePath

    fs.existsSync.mockReturnValue(true)

    jest.doMock(fakePackagePath, () => ({
      config: {
        projects: {
          'brave-core': {
            dir: 'src/brave',
            branch: 'master',
          },
        },
      },
    }), { virtual: true })

    // importa os módulos só depois do mock
    ;({ getNPMConfigFromPackageJson } = require('./util'))
    ;({ getNPMConfigFromPackageJsonOptmized } = require('./utilOptmized'))
  })

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
