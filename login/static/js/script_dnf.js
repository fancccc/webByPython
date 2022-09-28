$(function () {

	var defaultselectbox = $('#cusSelectbox');
	var numOfOptions = $('#cusSelectbox').children('option').length;
	/*
	var first = document.getElementById("cusSelectbox");
	var second = document.getElementById("cusSelectbox2");
	console.log(first)
	second.options.length = 0; // 清除second下拉框的所有内容
				if(first.selectedIndex == 0)
				{
					second.options.add(new Option("剑魂", "0", false, true));// 默认选中区
					second.options.add(new Option("狂战士", "1", )); 
					second.options.add(new Option("鬼泣", "2"));
					second.options.add(new Option("阿修罗", "3"));
					second.options.add(new Option("剑影", "4"));
				}

				if(first.selectedIndex == 1)
				{
					second.options.add(new Option("驭剑士", "0", false, true));// 默认选中区
					second.options.add(new Option("暗殿骑士", "1", )); 
					second.options.add(new Option("契魔者", "2"));
					second.options.add(new Option("流浪武士", "3"));
					second.options.add(new Option("刃影", "4"));
				}
				
				if(first.selectedIndex == 2)
				{
					second.options.add(new Option("气功师（男）", "0", false, true));// 默认选中区
					second.options.add(new Option("散打（男）", "1", )); 
					second.options.add(new Option("街霸（男）", "2"));
					second.options.add(new Option("柔道家（男）", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 3)
				{
					second.options.add(new Option("气功师（女）", "0", false, true));// 默认选中区
					second.options.add(new Option("散打（女）", "1", )); 
					second.options.add(new Option("街霸（女）", "2"));
					second.options.add(new Option("柔道家（女）", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 4)
				{
					second.options.add(new Option("漫游枪手（男）", "0", false, true));// 默认选中区
					second.options.add(new Option("枪炮师（男）", "1", )); 
					second.options.add(new Option("机械师（男）", "2"));
					second.options.add(new Option("弹药专家（男）", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 5)
				{
					second.options.add(new Option("漫游枪手（女）", "0", false, true));// 默认选中区
					second.options.add(new Option("枪炮师（女）", "1", )); 
					second.options.add(new Option("机械师（女）", "2"));
					second.options.add(new Option("弹药专家（女）", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 6)
				{
					second.options.add(new Option("元素爆破师", "0", false, true));// 默认选中区
					second.options.add(new Option("冰结师", "1", )); 
					second.options.add(new Option("血法师", "2"));
					second.options.add(new Option("逐风者", "3"));
					second.options.add(new Option("次元行者", "4"));
				}
				
				if(first.selectedIndex == 7)
				{
					second.options.add(new Option("元素师", "0", false, true));// 默认选中区
					second.options.add(new Option("召唤师", "1", )); 
					second.options.add(new Option("战斗法师", "2"));
					second.options.add(new Option("魔道学者", "3"));
					second.options.add(new Option("小魔女", "4"));
				}
				
				if(first.selectedIndex == 8)
				{
					second.options.add(new Option("圣骑士（男）", "0", false, true));// 默认选中区
					second.options.add(new Option("蓝拳圣使", "1", )); 
					second.options.add(new Option("驱魔师", "2"));
					second.options.add(new Option("复仇者", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 9)
				{
					second.options.add(new Option("圣骑士（女）", "0", false, true));// 默认选中区
					second.options.add(new Option("异端审判者", "1", )); 
					second.options.add(new Option("巫女", "2"));
					second.options.add(new Option("诱魔者", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 10)
				{
					second.options.add(new Option("刺客", "0", false, true));// 默认选中区
					second.options.add(new Option("死灵术士", "1", )); 
					second.options.add(new Option("忍者", "2"));
					second.options.add(new Option("影舞者", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 11)
				{
					second.options.add(new Option("精灵骑士", "0", false, true));// 默认选中区
					second.options.add(new Option("混沌魔灵", "1", )); 
					second.options.add(new Option("帕拉丁", "2"));
					second.options.add(new Option("龙骑士", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 12)
				{
					second.options.add(new Option("征战者", "0", false, true));// 默认选中区
					second.options.add(new Option("决战者", "1", )); 
					second.options.add(new Option("狩猎者", "2"));
					second.options.add(new Option("暗枪士", "3"));
					second.options.add(new Option("", "4"));
				}
				
				if(first.selectedIndex == 13)
				{
					second.options.add(new Option("暗刃", "0", false, true));// 默认选中区
					second.options.add(new Option("特工", "1", )); 
					second.options.add(new Option("战线佣兵", "2"));
					second.options.add(new Option("源能专家", "3"));
					second.options.add(new Option("", "4"));
				}		

				if(first.selectedIndex == 14)
				{
					second.options.add(new Option("缔造者", "0", false, true));// 默认选中区
					second.options.add(new Option("黑暗武士", "1", )); 
					second.options.add(new Option("", "2"));
					second.options.add(new Option("", "3"));
					second.options.add(new Option("", "4"));
				}
	*/				
	// hide select tag
	defaultselectbox.addClass('s-hidden');

	// wrapping default selectbox into custom select block
	defaultselectbox.wrap('<div class="cusSelBlock"></div>');

	// creating custom select div
	defaultselectbox.after('<div class="selectLabel"></div>');

	// getting default select box selected value
	$('.selectLabel').text(defaultselectbox.children('option').eq(0).text());

	// appending options to custom un-ordered list tag
	var cusList = $('<ul/>', { 'class': 'options'} ).insertAfter($('.selectLabel'));

	// generating custom list items
	for(var i=0; i< numOfOptions; i++) {
		$('<li/>', {
		text: defaultselectbox.children('option').eq(i).text(),
		rel: defaultselectbox.children('option').eq(i).val()
		}).appendTo(cusList);
	}

	// open-list and close-list items functions
	function openList() {
		for(var i=0; i< numOfOptions; i++) {
			$('.options').children('li').eq(i).attr('tabindex', i).css(
				'transform', 'translateY('+(i*100+100)+'%)').css(
				'transition-delay', i*30+'ms');
		}
	}

	function closeList() {
		for(var i=0; i< numOfOptions; i++) {
			$('.options').children('li').eq(i).css(
				'transform', 'translateY('+i*0+'px)').css('transition-delay', i*0+'ms');
		}
		$('.options').children('li').eq(1).css('transform', 'translateY('+2+'px)');
		$('.options').children('li').eq(2).css('transform', 'translateY('+4+'px)');
	}

	// click event functions
	$('.selectLabel').click(function () {
		$(this).toggleClass('active');
		if( $(this).hasClass('active') ) {
			openList();
			focusItems();
		}
		else {
			closeList();
		}
	});

	$(".options li").on('keypress click', function(e) {
		e.preventDefault();
		$('.options li').siblings().removeClass();
		closeList();
		$('.selectLabel').removeClass('active');
		$('.selectLabel').text($(this).text());
		defaultselectbox.val($(this).text());
		$('.selected-item p span').text($('.selectLabel').text());
	});
	
});

function focusItems() {

	$('.options').on('focus', 'li', function() {
		$this = $(this);
		$this.addClass('active').siblings().removeClass();
	}).on('keydown', 'li', function(e) {
		$this = $(this);
		if (e.keyCode == 40) {
			$this.next().focus();
			return false;
		} else if (e.keyCode == 38) {
			$this.prev().focus();
			return false;
		}
	}).find('li').first().focus();

};