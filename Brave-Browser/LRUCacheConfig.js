class LRUCacheConfig {
    #DEFAULT_LIMIT = 10;

    constructor(limit = this.#DEFAULT_LIMIT) {
        this.cache = new Map()
        this.limit = limit
    }

    get(key) {
        if(!this.cache.has(key)) return null
        const value = this.cache.get(key)
       
        this.cache.delete(key)
        this.cache.set(key, value)

        return value
    }

    set(key, value) {
        if (this.cache.has(key)) this.cache.delete(key)
        else if (this.cache.size >= this.limit) {
            const oldestKey = this.cache.keys().next().value
            this.cache.delete(oldestKey)
        }

        this.cache.set(key, value)
    }

    hasKey(key) {
        return this.cache.has(key)
    }

    getLimit() {
        return this.limit
    }
}

module.exports = LRUCacheConfig;