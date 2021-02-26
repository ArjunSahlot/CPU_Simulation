#!/bin/bash

download_link=https://github.com/ArjunSahlot/cpu_simulation/archive/main.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/cpu_simulation-main $1/cpu_simulation \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/cpu_simulation[0m"
