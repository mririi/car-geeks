const path = require('path');
const zlib = require("zlib");

module.exports = {
    devServer: {
        port: 8080
        
      },
    pluginOptions: {
        i18n: {
            locale: 'en',
            fallbackLocale: 'en',
            localeDir: 'locales',
            enableInSFC: false
        },
        compression:{
            brotli: {
              filename: '[file].br[query]',
              algorithm: 'brotliCompress',
              include: /\.(js|css|html|svg|json)(\?.*)?$/i,
              compressionOptions: {
                params: {
                  [zlib.constants.BROTLI_PARAM_QUALITY]: 11,
                },
              },
              minRatio: 0.8,
            },
            gzip: {
              filename: '[file].gz[query]',
              algorithm: 'gzip',
              include: /\.(js|css|html|svg|json)(\?.*)?$/i,
              minRatio: 0.8,
            }
          }
    },
    chainWebpack: config => {
        // Remove prefetch plugin and that's it!
        config.plugins.delete('prefetch');
    },
    configureWebpack: {
        resolve: {
            alias: {
                '@themeConfig': path.resolve(__dirname, 'theme.config.js'),                
            }
        }
    }

};
