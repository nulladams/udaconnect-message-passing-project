# set up the default terminal
ENV["TERM"]="linux"
Vagrant.configure("2") do |config|
  # set the image for the vagrant box
  config.vm.box = "opensuse/Leap-15.3.x86_64"
  # st the static IP for the vagrant box
  config.vm.network "private_network", ip: "192.168.56.4"
  # Forward the ports from the guest VM to the local host machine
  config.vm.network "forwarded_port", guest: 6443, host: 6443 # API Access
  # consifure the parameters for VirtualBox provider
  for p in 30000..30100 # expose NodePort IP's
    config.vm.network "forwarded_port", guest: p, host: p, protocol: "tcp"
    end
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 4
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
  end
  config.vm.provision "shell", inline: <<-SHELL
    sudo zypper refresh
    sudo zypper --non-interactive install bzip2
    sudo zypper --non-interactive install etcd
    sudo zypper --non-interactive install apparmor-parser
    # install a k3s cluster
    # curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.19.2+k3s1 K3S_KUBECONFIG_MODE="644" sh -
    # curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.19.3+k3s1 K3S_KUBECONFIG_MODE="644" sh -
    # curl -sfL https://get.k3s.io | sh -s -
    curl -sfL https://get.k3s.io | sh -
    # install iptables
    sudo zypper --non-interactive install iptables
    # install Helm
    curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
  SHELL
end