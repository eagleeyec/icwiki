# Awk

## Column filtering

### Column 6 regex match '10.'

    | awk '$6 ~ /^10\./'

### Column 8 not equals 5666

    | awk '$8 != 5666'
