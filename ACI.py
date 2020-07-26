---
- hosts: apic
  any_errors_fatal: true

  vars_files:
    - file-var.yml

  vars_prompt:
    - name: "apic_ip"
      prompt: "Enter APIC IP"
      private: no
  
    - name: "username"
      prompt: "Enter your APIC Username"
      default: 'admin'

    - name: "password"
      prompt: "Enter your APIC password"
      private: yes

  vars:
    ansible_connection: local
    connection: local
    ansible_python_interpreter: /usr/bin/python3
    aci_login: &aci_login
       hostname: '{{ inventory_hostname }}'
       username: '{{ username }}'
       password: '{{ password }}'

  tasks:
    - name: Create tenant
      aci_tenant:
        hostname: "{{ inventory_hostname }}"
        password: "{{ password }}"
        username: "{{ username }}"
        validate_certs: no
        tenant: "{{ item.tenant }}"
        validate_certs: no
        use_ssl: yes
        description: "{{ item.descri }}"
        state: present
      with_items: "{{ten}}"
      delegate_to: localhost
      tags: tenant

    - name: Add a new VRF to a tenant
      aci_vrf:
        hostname: "{{ inventory_hostname }}"
        password: "{{ password }}"
        username: "{{ username }}"
        validate_certs: no
        vrf: "{{ item.vrf }}"
        tenant: "{{ item.tenant }}"
        description: "{{ item.descri }}"
        state: present
      with_items: "{{vr}}"
      delegate_to: localhost
      tags: VRF

    - name: Add a new Bridge Domain
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


    - name: Create a subnet to Bridge Domain
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
