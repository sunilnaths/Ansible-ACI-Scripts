- name: Add a new VRF to a tenant
      aci_bd:
        hostname: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: no
        tenant: "{{ item.tenant }}"
        bd: "{{ item.bridge }}"
        vrf: "{{ item.vrf }}"
        description: "{{ item.descri }}"
        state: present
      with_items: "{{ Bri }}"
      delegate_to: localhost
      tags: BD


    - name: Create a subnet
      aci_bd_subnet:
        hostname: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        validate_certs: no
        tenant: "{{ item.tenant }}"
        bd: "{{ item.bridge }}"
        gateway: "{{ item.gateway }}"
        mask: "{{ item.mask }}"
        state: present
      with_items: "{{Bri}}"
      delegate_to: localhost
      tags: BD-SUB
