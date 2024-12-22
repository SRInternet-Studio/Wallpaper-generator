function showSubcategory(categoryId) {
    // 隐藏所有子分类
    const subcategories = document.querySelectorAll('.subcategory');
    subcategories.forEach(sub => sub.classList.add('hidden'));

    // 显示选中的子分类
    const selectedSubcategory = document.getElementById(`subcategory-${categoryId}`);
    if (selectedSubcategory) {
        selectedSubcategory.classList.remove('hidden');
    }
}
function showDetail(category, subcategory, tagName) {
    // 先隐藏所有三级菜单
    hideAllSubSubCategories();

    // 获取并显示对应的三级菜单
    const subSubCategory = document.getElementById(`subsubcategory-${category}-${subcategory}`);
    if (subSubCategory) {
        subSubCategory.classList.remove('hidden');
    }

    // 更新文本框显示，只显示英文部分
    if (tagName) {
        updateDisplay(tagName);
    }
}

function updateDisplay(tagName) {
    const selectedTextElement = document.getElementById('selected-text');
    let currentText = selectedTextElement.textContent.trim();
    let selectedTags = currentText ? currentText.split(', ') : [];

    // 只显示英文部分
    if (selectedTags.includes(tagName)) {
        selectedTags = selectedTags.filter(tag => tag !== tagName);
    } else {
        selectedTags.push(tagName);
    }

    selectedTextElement.textContent = selectedTags.join(', ');
}



function hideSubcategories() {
    // 隐藏所有二级菜单
    const subcategories = document.querySelectorAll('.subcategory');
    subcategories.forEach(subcategory => {
        subcategory.classList.add('hidden');
    });

    // 隐藏所有三级菜单
    const subsubcategories = document.querySelectorAll('.subsubcategory');
    subsubcategories.forEach(subsubcategory => {
        subsubcategory.classList.add('hidden');
    });
}
// 获取所有三级菜单按钮
const subSubCategoryButtons = document.querySelectorAll('.subsubcategory button');

// 绑定点击事件
subSubCategoryButtons.forEach(button => {
    button.addEventListener('click', () => {

        
        
        // 获取当前文本框中的内容
        let currentText = selectedTextElement.textContent.trim();
        
        // 将当前内容分割成数组，以便处理
        let selectedTags = currentText ? currentText.split(', ') : [];
        
        // 如果当前文本已在数组中，则将其移除
        if (selectedTags.includes(buttonText)) {
            selectedTags = selectedTags.filter(tag => tag !== buttonText);
        } else {
            // 否则，将文本添加到数组中
            selectedTags.push(buttonText);
        }
        
        // 更新文本框内容，多个标签用逗号分隔
        selectedTextElement.textContent = selectedTags.join(', ');
    });
});
// 函数：隐藏所有三级菜单
function hideAllSubSubCategories() {
    const subSubCategories = document.querySelectorAll('.subsubcategory');
    subSubCategories.forEach(subSubCategory => {
        subSubCategory.classList.add('hidden');
    });
}
function copyText() {
    const textBox = document.getElementById('selected-text');
    if (textBox) {
        // 为了支持 <div> 或其他非 <input> 元素的复制
        const range = document.createRange();
        range.selectNodeContents(textBox);
        const selection = window.getSelection();
        selection.removeAllRanges();  // 清除任何现有的选择
        selection.addRange(range);

        try {
            document.execCommand('copy');
            alert('复制成功');
        } catch (err) {
            console.error('复制失败：', err);
            alert('复制失败，请手动复制');
        }

        // 清除选择内容
        selection.removeAllRanges();
    } else {
        console.error('Text box not found');
    }
}


