public class EatHotpot {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i=0;i<n;i++){
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }
        // 设置吃菜时间
        int[] arrTime = new int[n];
        for (int i=0;i<n;i++){
            arrTime[i] = x[i]+y[i];
        }
        // 按吃菜时间从小到大排序
        Arrays.sort(arrTime);
        int pre = 0;
        int[] arrCount = new int[n];
        arrCount[0] = 1;
        for (int i=1;i<n;i++){
            // 判断arrTime是否是大于 上一个菜的时间+手速等待时间
            if (arrTime[i]>=(arrTime[pre]+m)){
                arrCount[i] = 1;
                pre = i;
            }
        }
        int count = 0;
        for (int i=0;i<n;i++){
            if (arrCount[i]>0){
                count++;
            }
        }
        System.out.println(count);
    }
}
