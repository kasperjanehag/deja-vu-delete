<template>
  <div>
    <v-treeview
      :items="treeData"
      item-key="name"
      activatable
      :open="open"
    >
      <template v-slot:prepend="{ item, open }">
        <v-icon v-if="item._isFile">
          insert_drive_file
        </v-icon>
        <v-icon v-else>
          {{ open ? 'folder_open' : 'folder' }}
        </v-icon>
      </template>
    </v-treeview>
  </div>
</template>

<script>
export default {
  props: ['files'],
  data() {
  return {
    open: [],
    files: [
      'folder1/file1.txt',
      'folder1/file2.txt',
      'folder1/subfolder1/file1.txt',
      'folder2/file1.txt'
    ]
  };
},
  computed: {
    treeData() {
      return this.buildFileTree(this.files);
    }
  },
  methods: {
    buildFileTree(paths) {
      let tree = {};
      paths.forEach(path => {
        let parts = path.split('/');
        let current = tree;
        parts.forEach((part, index) => {
          if (!current[part]) {
            current[part] = { _isFile: index === parts.length - 1, name: part, children: [] };
          }
          current = current[part].children;
        });
      });
      return Object.values(tree);
    },
  }
};
</script>