

<?php function isShow($url)
{
  $currentUrl = $_SERVER['REQUEST_URI'];
  $path = parse_url($currentUrl, PHP_URL_PATH);
  return ($url === $path) ? 'show' : '';
}?>


<li class="nav-item">
  <a data-bs-toggle="collapse" href="#applicationsExamples" class="nav-link active" aria-controls="applicationsExamples" role="button" aria-expanded="false">
    <div class="icon icon-shape icon-sm shadow border-radius-md bg-white text-center d-flex align-items-center justify-content-center  me-2">
      <svg width="12px" height="12px" viewBox="0 0 40 40" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <title><?php // echo $usuario['rol'] ?></title>
        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
          <g transform="translate(-2020.000000, -442.000000)" fill="#FFFFFF" fill-rule="nonzero">
            <g transform="translate(1716.000000, 291.000000)">
              <g transform="translate(304.000000, 151.000000)">
                <polygon class="color-background" opacity="0.596981957" points="18.0883333 15.7316667 11.1783333 8.82166667 13.3333333 6.66666667 6.66666667 0 0 6.66666667 6.66666667 13.3333333 8.82166667 11.1783333 15.315 17.6716667"></polygon>
                <path class="color-background" d="M31.5666667,23.2333333 C31.0516667,23.2933333 30.53,23.3333333 30,23.3333333 C29.4916667,23.3333333 28.9866667,23.3033333 28.48,23.245 L22.4116667,30.7433333 L29.9416667,38.2733333 C32.2433333,40.575 35.9733333,40.575 38.275,38.2733333 L38.275,38.2733333 C40.5766667,35.9716667 40.5766667,32.2416667 38.275,29.94 L31.5666667,23.2333333 Z" opacity="0.596981957"></path>
                <path class="color-background" d="M33.785,11.285 L28.715,6.215 L34.0616667,0.868333333 C32.82,0.315 31.4483333,0 30,0 C24.4766667,0 20,4.47666667 20,10 C20,10.99 20.1483333,11.9433333 20.4166667,12.8466667 L2.435,27.3966667 C0.95,28.7083333 0.0633333333,30.595 0.00333333333,32.5733333 C-0.0583333333,34.5533333 0.71,36.4916667 2.11,37.89 C3.47,39.2516667 5.27833333,40 7.20166667,40 C9.26666667,40 11.2366667,39.1133333 12.6033333,37.565 L27.1533333,19.5833333 C28.0566667,19.8516667 29.01,20 30,20 C35.5233333,20 40,15.5233333 40,10 C40,8.55166667 39.685,7.18 39.1316667,5.93666667 L33.785,11.285 Z"></path>
              </g>
            </g>
          </g>
        </g>
      </svg>
    </div>
    <span class="nav-link-text ms-1">Administradores</span>
  </a>
  <div class="collapse  show " id="applicationsExamples">
    <ul class="nav ms-4 ps-3">
      <li class="nav-item ">
        <a class="nav-link " href="../../pages/applications/kanban.html">
          <span class="sidenav-mini-icon"> D </span>
          <span class="sidenav-normal"> Dashboard </span>
        </a>
      </li>
      <li class="nav-item ">
        <a class="nav-link <?php //echo isActive('/admin') ?> " data-bs-toggle="collapse" aria-expanded="false" href="#productsExample">
          <span class="sidenav-mini-icon"> P </span>
          <span class="sidenav-normal">Admin-Productos</span>
        </a>
        <div class="collapse  <?php //echo isShow('/admin/lista_productos.php') ?> " id="productsExample">
          <ul class="nav nav-sm flex-column">
            <li class="nav-item">
              <a class="nav-link <?php //echo isActive('/admin/lista_productos.php') ?>" href="/admin/lista_productos.php">
                <span class="sidenav-mini-icon text-xs"> P </span>
                <span class="sidenav-normal"> Lista de Productos </span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link " href="/admin/cargar_categoria.php">
                <span class="sidenav-mini-icon text-xs"> C </span>
                <span class="sidenav-normal"> Lista de Categorias </span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link " href="/admin/lista_publicados.php">
                <span class="sidenav-mini-icon text-xs"> P </span>
                <span class="sidenav-normal"> Lista de Publicados </span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/admin/lista_pedidos.php">
                <span class="sidenav-mini-icon text-xs"> P </span>
                <span class="sidenav-normal"> Lista de Pedidos </span>
              </a>
            </li>
          </ul>
        </div>
      <li class="nav-item ">
        <a class="nav-link collapsed" data-bs-toggle="collapse" aria-expanded="false" href="#usersExample">
          <span class="sidenav-mini-icon"> U </span>
          <span class="sidenav-normal"> Usuario <b class="caret"></b></span>
        </a>
        <div class="collapse" id="usersExample">
          <ul class="nav nav-sm flex-column">
            <li class="nav-item">
              <a class="nav-link " href="../../../pages/pages/users/reports.html">
                <span class="sidenav-mini-icon text-xs"> R </span>
                <span class="sidenav-normal"> Reports Clientes </span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link " href="../../../pages/pages/users/new-user.html">
                <span class="sidenav-mini-icon text-xs"> A </span>
                <span class="sidenav-normal"> Admin-Usuario</span>
              </a>
            </li>
          </ul>
        </div>
      </li>
      <li class="nav-item ">
        <a class="nav-link " href="../../pages/applications/calendar.html">
          <span class="sidenav-mini-icon"> C </span>
          <span class="sidenav-normal"> Configuraciones </span>
        </a>
      </li>
      <li class="nav-item ">
        <a class="nav-link " href="../../pages/applications/analytics.html">
          <span class="sidenav-mini-icon"> S </span>
          <span class="sidenav-normal"> Soporte </span>
        </a>
      </li>
    </ul>
  </div>
</li>