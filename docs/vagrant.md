# Vagrant

## Example config

    VAGRANTFILE_API_VERSION = "2"

    Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
        config.vm.box = "centos/7"
        config.vm.network "private_network", ip: "192.168.33.10"
        config.vm.network "public_network"
        config.vm.provider "virtualbox" do |vb|
   	 	  # Use the host DNS
   	 	  vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
          vb.memory = "3096"
        end
    end

## Setup Guest Additions

	vagrant plugin install vagrant-vbguest
	# OR
	vagrant plugin update vagrant-vbguest
	# Or if it is still not playing nice
	vagrant vbguest --do install --no-cleanup; vagrant ssh -c 'yes | sudo /mnt/VBoxLinuxAdditions.run'

