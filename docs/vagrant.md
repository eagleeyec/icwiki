# Vagrant

## Example config

    VAGRANTFILE_API_VERSION = "2"

    Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
        config.vm.box = "centos/7"
        config.vm.network "private_network", ip: "192.168.33.10"
        config.vm.network "public_network"
        config.vm.provider "virtualbox" do |vb|
          vb.memory = "3096"
        end
    end
