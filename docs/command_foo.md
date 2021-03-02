# Command Foo

## Get my public IP address

    curl http://ipecho.net/plain

## Parse html xpath content from curl

You can inspect a page in chrome to find the xpath you need to access a part of the page, then run like:

    curl -s -L -k https://somewhere.com/some_page | xmllint --xpath "/html/body/h2[1]" -

You get just the specific html part back. Makes greping for a particular part more accurate.
