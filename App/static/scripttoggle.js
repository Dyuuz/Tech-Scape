// JavaScript to toggle the Like and Bookmark button states
let isLiked = false;
let isBookmarked = false;

function toggleLike() {
    const likeButton = document.querySelector('.post-likes');
    const likeCount = document.getElementById('like-count');

    isLiked = !isLiked;
    likeButton.classList.toggle('active', isLiked);
    likeCount.textContent = isLiked ? parseInt(likeCount.textContent) + 1 : parseInt(likeCount.textContent) - 1;
}

function toggleBookmark() {
    const bookmarkButton = document.querySelector('.post-bookmark');
    isBookmarked = !isBookmarked;
    bookmarkButton.classList.toggle('active', isBookmarked);
}

function toggleShareDropdown() {
    const shareContainer = document.querySelector('.post-share-container');
    shareContainer.classList.toggle('active');
}

        