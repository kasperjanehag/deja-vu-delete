async function findDuplicates() {
    let duplicates = await eel.find_duplicates_python()();
    console.log(duplicates);
    // Further processing to display duplicates
}

async function populateFileList() {

    console.log("Starting to populate file list...");
    let files = await eel.list_images()();
    console.log("Received files: ", files);


    let fileTree = document.getElementById('fileTree');
    fileTree.innerHTML = ''; // Clear existing tree

    let treeData = buildFileTree(files);
    console.log("Built tree data: ", treeData);

    createTree(fileTree, treeData);
    console.log("Created tree with data");
}

function buildFileTree(paths) {
    let tree = {};
    paths.forEach(path => {
        let parts = path.split('/');
        let current = tree;
        parts.forEach((part, index) => {
            if (!current[part]) {
                current[part] = { _isFile: index === parts.length - 1 };
            }
            current = current[part];
        });
    });
    return tree;
}

function createTree(domElement, treeData, level = 0) {
    Object.keys(treeData).forEach(key => {
        if (key === '_isFile') {
          return;
        }

        let div = document.createElement('div');
        div.className = 'tree-node';
        div.style.paddingLeft = `${level * 20}px`;
        div.textContent = key;

        if (!treeData[key]._isFile) { // Check if it's not a file
            div.onclick = function () {
                this.classList.toggle('collapsed');
            };
            div.classList.add('collapsible');
        }

        let children = treeData[key];
        let childContainer = document.createElement('div');
        childContainer.className = 'child-container';
        createTree(childContainer, children, level + 1);
        div.appendChild(childContainer);

        domElement.appendChild(div);
    });
}

// Call this function when the page loads
populateFileList();
