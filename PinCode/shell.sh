#!/bin/bash

read -p "# " command

if [[ $command == *"bash"* ]] || 
   [[ $command == *"sh"* ]] || 
   [[ $command == *"python"* ]] || 
   [[ $command == *"perl"* ]] || 
   [[ $command == *"go"* ]] || 
   [[ $command == *"base64"* ]] || 
   [[ $command == *"chmod"* ]] || 
   [[ $command == *"?"* ]] || 
   [[ $command == *"*"* ]]; then
    echo "Disallowed command!"
    exit
fi

eval "$command"

exit
