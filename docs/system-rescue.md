# System rescue

## Prep raid for mounting
    mdadm --examine --scan >> /etc/mdadm.conf
    mdadm --assemble --scan /dev/md/pv00
    mdadm --assemble --scan /dev/md/boot

## Prep LVM for mounting
    vgchange -ay

## Mount the volumes
    mount /dev/mapper/centos-root /mnt
    mount /dev/md126 /mntboot # sometimes this is md127

## Prepare for making grub
    mount --bind /dev /mnt/dev
    mount --bind /proc /mnt/proc
    mount --bind /sys /mnt/sys
    chroot /mnt

## Make grub
    awk -F\' '$1=="menuentry " {print $2}' /etc/grub2.cfg
    grub2-set-default 0
    grub2-mkconfig -o /boot/grub2/grub.cfg
